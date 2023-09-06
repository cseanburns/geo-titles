## Countries and Journal Impact

```{r tabularize-nations, include = FALSE}
median(with_nations$HDI)
titles %>% dplyr::select(nation) %>% table %>% as.data.frame()
with_nations %>% dplyr::select(nation) %>% table %>% as.data.frame()
```

```{r uniq-nations, include = FALSE}
uniq_count <- titles %>% dplyr::select(nation) %>%
  dplyr::filter(nation != "NA") %>%
  unique() %>% count()
```

```{r top-20-nations, echo = FALSE}
my_tab <- with_nations %>%
  dplyr::filter(nation != "NA" & HDI != "NA") %>%
  dplyr::select(nation, HDI) %>% table
wn_df <- my_tab %>% as.data.frame %>%
  dplyr::arrange(desc(Freq)) %>% dplyr::filter(Freq > 0)
my_tab_20 <- my_tab %>% as.data.frame %>%
  dplyr::arrange(desc(Freq)) %>% slice_head(n = 20)
```

There were `r uniq_count` country names or country name combinations
identified in the `r length(with_nations$nation)` articles with country
names in titles.
Out of these, `r dim(my_tab)[1]` had HDI scores assigned to them.
China appeared in titles most frequently, followed by Spain, the U.S.A.,
the European Union, the United Kingdom, and India.
The median HDI for the observed countries is
`r median(with_nations$HDI)`.
Therefore, most identified countries are
classified as having very high human development index scores
(*min* = `r min(with_nations$HDI)`,
*m* = `r round(mean(with_nations$HDI),3)`,
*max* = `r max(with_nations$HDI)`).
Table 1 lists the `r dim(my_tab_20)[1]` most
frequently referenced country names in titles along with their
respective HDI scores.

```{r top-20-nations-table, echo = FALSE}
my_tab_20 %>% 
  kable(caption = "Table 1. Top 20 countries in article titles")
rm(my_tab)
```

### Journals with Articles with Country Names in Titles Receiver Fewer Citations

Journals that receive SJR scores above 1.0 indicate journals that
receive above average citations compared to all journals in *Scopus*.
The average SJR for all the journals in our data was slightly above the
*Scopus* average (*mdn* = `r median(titles$SJR)`). We sought to test
whether country names in article titles had an impact on journal
citations. We divided the data into two groups: articles with country
names referenced in titles and articles without country names referenced
in titles. We compared the SJR of the journals between these two groups.
Even though there are journal titles that belong to both groups, our
goal was to observe the effect that country names have on overall
journal citations.

We found that the inclusion of country names in article titles had a
negative effect on citations to journals. The average SJR for journals
that published articles that did not include references to country names
was higher (*mdn* = `r median(without_nations$SJR)`) than the SJR
average. However, the average SJR for journals that published articles
that did include references to countries was lower than the *Scopus*
average and lower than journals with articles without references to
countries (*mdn* = `r median(with_nations$SJR)`). Overall, this suggests
that journals that tend to publish articles with titles containing
references to countries receive fewer citations than journals that tend
to publish articles to do not reference countries. Table 2 reports the
journal titles that most frequently publish articles that reference
country names in article titles.

```{r get-summaries, include = FALSE}
summary(titles$SJR)
summary(with_nations$SJR)
summary(without_nations$SJR)
```

```{r get-SJRs, include = FALSE}
titles %>% dplyr::select(Publication) %>% table %>% as.data.frame() %>%
  dplyr::arrange(desc(Freq)) %>% slice_head(n = 20)
with_nations %>% dplyr::select(SJR) %>% table %>% as.data.frame() %>%
  dplyr::arrange(desc(Freq)) %>% slice_head(n = 20)
```

```{r get-table-2, echo = FALSE}
my_tab <- titles %>%
  dplyr::filter(nation != "NA" & HDI != "NA") %>%
  dplyr::select(Publication, SJR) %>% table
my_tab <- my_tab %>% as.data.frame %>%
  dplyr::arrange(desc(Freq)) %>% slice_head(n = 20)
my_tab %>%
  kable(caption = "Table 2. Top 20 most frequent journal titles with countries mentioned in titles")
```

```{r get-wt-test-1, include = FALSE}
# SJR differences between country and non-country data subsets
summary(with_nations$SJR)
sd(with_nations$SJR)
summary(without_nations$SJR)
sd(without_nations$SJR)
nations_wt <- wilcox.test(with_nations$SJR, without_nations$SJR)
nations_cd <- cliff.delta(with_nations$SJR, without_nations$SJR)
```

We compared the average SJR of journals with articles with country names
in titles to the SJR of journals without country names in articles using
a Wilcoxon rank-sum test. The test revealed a significant difference (W
= `r nations_wt$statistic`, p \< `r round(nations_wt$p.value, 3)`, *n*
with place names = `r dim(with_nations)[1]` *n* without place names =
`r dim(without_nations)[1]`). However, even though articles without
countries in titles published in lower impact journals, the overall
effect size was small (Cliff's delta = `r nations_cd$estimate`, 95% CI
[`r nations_cd$conf.int[1]`, `r nations_cd$conf.int[2]`]).

```{r group-data, include = FALSE}
sjr_df<- data.frame(
  group = c(rep("With Countries", length(with_nations$SJR)),
            rep("Without Countries", length(without_nations$SJR))),
  score = c(with_nations$SJR, without_nations$SJR)
)
```

```{r fig-1, fig.cap = "Fig. 1: Comparison of Journal Impacts Scores", echo = FALSE}
ggplot(sjr_df, aes(x = group, y = score)) +
  geom_boxplot() +
  labs(x = "Groups", y = "Journal Impact (SJR)") +
  theme_minimal()
```

### Lower impact journals publish more articles with country names in titles

We suspected that journals with lower impact scores publish more
articles with place names in titles. Therefore we partitioned the list
of articles with places names in titles into three subsets: set1
contains articles in journals with less than the median SJR, set2
contains articles in journals with greater than the median SJR, and set3
contains articles in journals equal to SJR median.

```{r compare-median-SJRs, include = FALSE}
SJR_med             <- with_nations %>% mutate(med = median(SJR))
less_than_median    <- SJR_med %>% dplyr::filter(SJR < med)
greater_than_median <- SJR_med %>% dplyr::filter(SJR > med)
equal_to_median     <- SJR_med %>% dplyr::filter(SJR == med)
grlt_wt <- wilcox.test(greater_than_median$SJR, less_than_median$SJR)
```

Although some articles with countries named in titles were published in
journals with SJRs equal to the median (*n* =
`r length(equal_to_median$SJR)`; *mdn* =
`r median(equal_to_median$SJR)`), we found that articles with country
names in titles were less likely to appear in journals with above median
SJR scores (*n* = `r length(greater_than_median$SJR)`; *mdn* =
`r median(greater_than_median$SJR)`) and more likley to appear in
journals with below median SJR scores (*n* =
`r length(less_than_median$SJR)`; *mdn* =
`r median(less_than_median$SJR)`).

We applied a Wilcoxon ran-sum test to compare the below and above median
groups. The test revealed a significant difference (W =
`r grlt_wt$statistic`; *p* \< `r round(grlt_wt$p.value, 3)`), indicating
that journals with higher SJR scores publish fewer articles with country
names in titles.

```{r publication-sorting, echo = FALSE}
SJR_journals_with <- titles %>% arrange(Publication) %>%
  dplyr::filter(nation != "NA" & HDI != "NA") %>%
  dplyr::select(Publication, SJR)
```

```{r fig-2a, echo = FALSE}
testdf1 <- unique(SJR_journals_with)
testdf2 <- table(SJR_journals_with$Publication)
testdf2 <- as.data.frame(testdf2)
testdf1$Freq <- testdf2$Freq
testdf1 <- testdf1 %>% dplyr::arrange(desc(Freq))
```

```{r get-non-title-data, echo = FALSE}
SJR_journals_without <- titles %>% 
  dplyr::filter(is.na(nation)) %>%
  dplyr::select(Publication, SJR) %>%
  arrange(Publication)
```

```{r fig-2b, echo = FALSE}
testdf3 <- unique(SJR_journals_without)
testdf4 <- table(SJR_journals_without$Publication)
testdf4 <- as.data.frame(testdf4)
testdf3$Freq <- testdf4$Freq
testdf3 <- testdf3 %>% dplyr::arrange(desc(Freq))
```

```{r fig-2, echo = FALSE, fig.cap = "Fig. 2: Articles and SJR"}
testdf1$Country <- "with_country"
testdf3$Country <- "without_country"
combined_df <- bind_rows(testdf1, testdf3)
ggplot(combined_df, aes(x = SJR, y = Freq, size = Freq, color = Country)) + geom_point(alpha = 0.5) + theme_light() + scale_color_grey()
```

## Countries and Article Impact

```{r get-wt-test-2, include = FALSE}
# citation differences between country and non-country data subsets
summary(with_nations$Citations)
sd(with_nations$Citations)
summary(without_nations$Citations)
sd(without_nations$Citations)
citations_wt <- wilcox.test(with_nations$Citations, without_nations$Citations)
citations_cd <- cliff.delta(with_nations$Citations, without_nations$Citations)
```

We found that article titles with country names are more likely to have
lower citation counts than article titles without country names. A
Wilcoxon rank-sum test was conducted to compare the median citation
counts. Articles with countries referenced in titles received fewer
citations (*mdn* = `r median(with_nations$Citations)`) than articles
without references to countries in titles (*mdn* =
`r median(without_nations$Citations)`). The test revealed a significant
difference between the two groups (W = `r citations_wt$statistic`, *p* =
`r round(citations_wt$p.value, 3)`, *n* with place names =
`r length(with_nations$Citations)`, *n* without place names =
`r length(without_nations$Citations)`). These results suggest that
papers without place names in titles received more citations, in
general, than papers with place names in titles. However, the effect
size was small. We used Cliff's delta to assess the magnitude of the
difference in scores between papers with place names in titles to papers
without place names in titles. The analysis revealed a negligible effect
size in favor of papers without place names in titles (delta =
`r citations_cd$estimate`, 95% CI [`r citations_cd$conf.int`]).

```{r group-citation-data, echo = FALSE}
citations_df <- data.frame(
  group = c(rep("With Countries", length(with_nations$Citations)),
            rep("Without Countries", length(without_nations$Citations))),
  score = c(log(with_nations$Citations + 1),
            log(without_nations$Citations + 1)
))
```

```{r fig-4, echo = FALSE, fig.cap = "Fig. 4: Comparison of Citations"}
ggplot(citations_df, aes(x = group, y = score)) +
  geom_boxplot() +
  labs(x = "Groups", y = "Citations (log + 1 transformed)") +
  theme_minimal()
```

## Countries and HDIs

```{r get-regression, include = FALSE}
less_HDI <- with_nations %>%
  dplyr::select(HDI) %>% dplyr::filter(HDI < median(HDI)) %>% tally()
great_HDI <- with_nations %>%
  dplyr::select(HDI) %>% dplyr::filter(HDI > median(HDI)) %>% tally()
fit.1 <- lm(log(with_nations$Citations + 1) ~ with_nations$HDI)
fit.cit2hdi <- summary(fit.1)
fstatistic <- fit.cit2hdi$fstatistic
p_value_fstatistic <- pf(fstatistic[1], fstatistic[2],
                         fstatistic[3], lower.tail = FALSE)
```

Countries with below median HDI scores (*n* = `r less_HDI`) were as
likely to appear in article titles as countries with higher HDI scores
(*n* = `r great_HDI`). A linear regression analysis was conducted to
examine the relationship between HDI and citations for articles that
reference country names in titles. The regression equation was not
significant (F-statistic: `r round(fit.cit2hdi$fstatistic[1], 3)`, *p* =
`r round(p_value_fstatistic, 3)`, R-squared \<
`r round(fit.cit2hdi$r.squared, 3)`), and the results indicated that the
HDI was not a significant predictor of citation counts (t-value =
`r round(fit.cit2hdi$coefficients[2,3], 3)`, *p* =
`r round(fit.cit2hdi$coefficients[2,4], 3)`, *b* =
`r round(fit.cit2hdi$coefficients[2], 3)`). We therefore found no
significant effect on whether the HDI of the named country in an article
title had an effect on the number of citations the article received.

```{r fig-5, echo = FALSE, message = FALSE, fig.cap = "Fig. 5: HDI to Citations"}
ggplot(with_nations, aes(x = HDI, y = log(Citations + 1))) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  labs(x = "HDI", y = "Citations (log + 1)") +
  theme_light()
```

```{r prep-table-3, echo = FALSE}
my_tab <- with_nations %>% arrange(desc(Citations)) %>%
  select(nation, Citations, SJR, HDI) %>%
  slice_head(n = 20)
```

```{r table-3, echo = FALSE}
my_tab %>%
  kable(caption = "Table 3. Papers with countries named or referred to with highest citations")
rm(my_tab)
```

## Country Naming and Semantic Value

We examined where the location of countries appeared in article titles
under the assumption that countries appearing near the end of a title
provided little informational value to the idea expressed in the first
part of the title.

```{r get-position-correlation, include = FALSE}
summary(titles$places)
titles_place_pos_citations <- titles %>%
  dplyr::select(Citations, places) %>%
  dplyr::filter(places != "NA")
places_cor <- cor(titles_place_pos_citations$Citations,
                  titles_place_pos_citations$places, method = "spearman")
```

On average, countries tended to be referenced near the end of a title
(*m* = `r round(mean(titles$places, na.rm = TRUE), 3)`, *mdn* =
`r median(titles$places, na.rm = TRUE)`), suggesting that most articles
that contain names of countries in the data do so without adding much
semantic information to the title. A Spearman's rank correlation was
computed to compare the location of the country name in a title and the
citations received to the articles with country names in titles. We
found no relationship (*r* = `r round(places_cor, 3)`).

```{r fig-6, echo = FALSE, message = FALSE, fig.cap = "Fig. 6: Title Place Position and Citations"}
ggplot(titles_place_pos_citations, aes(x = places,
                                       y = log(Citations + 1))) +
  geom_point() +
  theme_minimal()
```

```{r fig-7, fig.cap = "Fig. 7: Publications with countries listed in articles", echo = FALSE, message = FALSE}
pubs <- titles %>% dplyr::select(Publication, HDI, SJR, nation) %>%
  dplyr::filter(nation != "NA" & HDI != "NA")
ggplot(pubs, aes(x = HDI, y = Publication, fill = SJR)) +
  geom_density_ridges_gradient()
```


