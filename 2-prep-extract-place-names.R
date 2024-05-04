library(spacyr)
library(dplyr)

titles <- read.table(file = "data/titles.csv", header = FALSE,
                     sep = ",", quote = "\"",
                     row.names = NULL,
                     col.names = c("Citations", "Titles", "Journals"),
                     na.strings = "NA",
                     stringsAsFactors = FALSE)

titles$id <- row.names(titles)

titles$Titles   <- tolower(titles$Titles)
titles$Journals <- tolower(titles$Journals) 

# get character length of each title in data frame
titles$titles_cnt <- nchar(titles$Titles[1:length(titles$Titles)])

# identify place names in titles
spacy_initialize()

titles_sparsed <- spacy_parse(titles$Titles, entity = TRUE)

titles$doc_id <- unique(titles_sparsed$doc_id)

token <- titles_sparsed %>%
    dplyr::select(doc_id, token, entity) %>%
    dplyr::filter(entity == "GPE_B") %>%
    dplyr::select(doc_id, token)

titles <- dplyr::full_join(token, titles, by = "doc_id")

titles$titles_has_country <- is.na(titles$token)
titles_with_country <- titles %>%
    dplyr::filter(titles_has_country == "FALSE")
titles_without_country <- titles %>%
    dplyr::filter(titles_has_country == "TRUE")

spacy_finalize()

# Find the position of the token within the title
get_character_count <- function(title, token) {
    match_pos <- regexpr(token, title)
              
    # Return NA if the token is not found in the title;
    # Else, return the position of the first occurrence of token in title
    if (match_pos == -1) {
        return(NA)
    } else {
        return(match_pos)
    }
}

# Create vector with numerical title position
titles_with_country$pos <- mapply(get_character_count,
                                  titles_with_country$Titles,
                                  titles_with_country$token)

titles_with_country$prop <- titles_with_country$pos / titles_with_country$titles_cnt

# Create empty vectors before joining
titles_without_country$pos <- "NA"
titles_without_country$prop <- "NA"

# combine and sort data frame
titles <- rbind(titles_with_country, titles_without_country)
titles$id <- as.integer(titles$id)
titles <- titles[order(titles$id, decreasing = FALSE), ]

titles$pos <- as.numeric(titles$pos)
titles$prop <- as.numeric(titles$prop)

write.table(titles, file = "data/titles.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE)

# remove intermediary objects
rm(get_character_count, titles_sparsed, titles_with_country,
   titles_without_country, token, titles)
