# Descriptive statistics
library(tidyverse)
library(conflicted)
library(kableExtra)

# Import data
titles <- read.csv("~/workspace/geo-titles/data/titlesMain.csv")

# Get frequency of nations listed in titles
my_tab <- table(titles$nation)
my_tab2 <- my_tab[order(my_tab, decreasing = TRUE)]
my_tab2
