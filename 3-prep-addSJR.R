# Exporting and importing data to add HDIs for each nation listed and SJR for
# each publication title; used LibreOffice Calc; thus non-automated;
# titlesMain.csv becomes the main data file

# save publication title data as separate data frame/tibble
# and convert to tibble to export as CSV file to add SJR data
pubtitles <- tibble(SO = data$SO)
write.table(pubtitles, file = "data/pubtitles.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE,
            col.names = FALSE)

# Export to add publication titles and clean up data
titlesHDI <- read.csv("data/titles-hdi-citations.csv",
                      header = TRUE, sep = ",")
titlesHDI$No <- NULL
write.table(titlesHDI, file = "data/titlesHDI.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE,
            col.names = TRUE)

# Replace empty strings in selected columns with NA
titlesHDI <- read.csv("data/titlesHDI.csv",
                      header = TRUE,
                      sep = ",")
titlesHDI["CountryRegion"][titlesHDI["CountryRegion"] == ''] <- NA
titlesHDI["Averaged"][titlesHDI["Averaged"] == ''] <- NA

# export to add SJR (controlling for journal impact in model)
write.table(titlesHDI, file = "data/titlesHDI.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE,
            col.names = TRUE)
titlesMain <- read.csv("data/titlesHDI.csv",
                       header = TRUE, sep = ",")

