library(bibliometrix)
library(tidyverse)

data <- convert2df(file = "data/lisjournals.bib", dbsource = "scopus", format = "bibtex")
titles <- tibble(TC = data$TC, TI = data$TI)
write.table(titles, file = "titles.csv", quote = TRUE, sep = ",", row.names = FALSE, col.names = FALSE)
