# Manually identified titles with false negatives and manually created tokens
# this script will capture the position of the first token
# and calucate its position in the article title

false_negatives <- read.csv(file = "data/false_negs.csv",
                            header = TRUE,
                            sep = ",",
                            quote = "\"")

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
false_negatives$pos <- mapply(get_character_count,
                                  false_negatives$Titles,
                                  false_negatives$token)

false_negatives$prop <- false_negatives$pos / false_negatives$titles_cnt

write.table(false_negatives, file = "data/false_negatives_prop_data.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE)

# cleanup
rm("false_negatives","get_character_count","titles")
save.image()
