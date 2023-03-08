library(bibliometrix)
library(tidyverse)

# source data is from Scopus
data <- convert2df(file = "data/lisjournals.bib", dbsource = "scopus", format = "bibtex")

# save title and citation count as separate data frame/tibble
# convert to tibble from bib to export as CSV file
titles <- tibble(TC = data$TC, TI = data$TI)

# save as CSV file to read into Python for geocoding
write.table(titles, file = "data/titles.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE, col.names = FALSE)
