# save publication title as separate data frame/tibble
# convert to tibble from from bib to export as CSV file
pubtitles <- tibble(SO = data$SO)
write.table(pubtitles, file = "data/pubtitles.csv", quote = TRUE, sep = ",", row.names = FALSE, col.names = FALSE)

# Export to add publication titles and clean up data
titlesHDI <- read.csv("data/titles-hdi-citations.csv", header = TRUE, sep = ",")
titlesHDI$No <- NULL
write.table(titlesHDI, file = "data/titlesHDI.csv", quote = TRUE, sep = ",", row.names = FALSE, col.names = TRUE)
# Replace empty strings in selected columns with NA
titlesHDI <- read.csv("data/titlesHDI.csv", header = TRUE, sep = ",")
titlesHDI["CountryRegion"][titlesHDI["CountryRegion"] == ''] <- NA
titlesHDI["Averaged"][titlesHDI["Averaged"] == ''] <- NA

# export to add SJR (controlling for journal impact in model)
write.table(titlesHDI, file = "data/titlesHDI.csv", quote = TRUE, sep = ",", row.names = FALSE, col.names = TRUE)
titlesMain <- read.csv("data/titlesHDI.csv", header = TRUE, sep = ",")

