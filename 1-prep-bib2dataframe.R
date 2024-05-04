library(bibliometrix)
library(tidyverse)

# source data is from Scopus
data <- convert2df(file = "data/lisJournals_no_translations.bib",
                   dbsource = "scopus", format = "bibtex")

# save citation count, title, and journal name as separate data frame
# convert to tibble from bib to export as CSV file
titles <- tibble(TC = data$TC, TI = data$TI, SO = data$SO)

# save as CSV file to read into R for geocoding
write.table(titles, file = "data/titles.csv",
            quote = TRUE, sep = ",",
            row.names = FALSE, col.names = FALSE)
