# Title Study of LIS Journals

Burns, C.S., &amp; Islam, M.A. (2024).
A citation analysis examining geographical specificity in article titles.
*Scientometrics*.
[https://doi.org/10.1007/s11192-024-05075-3](https://doi.org/10.1007/s11192-024-05075-3) ;
Code and data:
[https://github.com/cseanburns/geo-titles](https://github.com/cseanburns/geo-titles)

Preprint:

Burns, C.S., & Islam, M.A. (*Forthcoming*). A citation analysis examining geographical specificity in article titles. *Scientometrics*.

The preprint is version one. The final manuscript was substantially revised:

Preprint: https://doi.org/10.21203/rs.3.rs-3605640/v1

## Data notes

### Date: 2024-05-04

* removed all article title translations from **lisjournals.bib** (the original Scopus *bib* file)
    - saved this as **lisJournals_no_translations.bib**
    - used **lisJournals_no_translations.bib** as the main data file
- imported the above **bib** file into R using the `bibliometrix` R package
- created `titles` dataframe using only the following variables:
    - TC = times cited
    - TI = article title
    - SO = publication title
- replaced Spacy Python code with Spacy R code using the `spacyr` package 
- used R and `spacyr` to:
    - calculate the number of characters in article titles
    - identify geopolitical entities in article titles
    - identify the character position of first geopolitical entity (GPE) in article titles
    - calculate the GPE character positions out of the total characters in article titles
    - exported the `titles` dataframe to a CSV file
- used LibreOffice Calc to manually scan the `titles` CSV file.
    - GPEs identified by `spacyr` were inconsistent but kept in the vector named `token`
    - Created a vector called `False_Positive`
    - Created a vector called `GPE` to label the correct geopolitical entity
- `spacyr` created duplicate entries when titles contained more than one GPE
    - identified and removed duplicated entries
    - kept entry where GPE first appeared since this effects the character position of the GPE in the title
    - removed data for `pos` and `prop` for records that were false positives
- the `titles_has_country` vector:
    - reversed TRUE and FALSE
    - TRUE = 1
    - FALSE = 0
- removed journals that were mostly outside the social sciences
    - journal of chemical information and modeling
    - journal of cheminformatics
    - ieee transactions on information theory
    - journal of classification
    - scientific data 
- country, HDI notes
    - id 5813 included Jordan and Gaza. We just included HDI information for Jordan
    - Used Albania HDI for Kosovo
    - For Taiwan, used .926 https://en.wikipedia.org/wiki/List_of_administrative_divisions_of_Greater_China_by_Human_Development_Index
    - For Aruba, used https://en.populationdata.net/rankings/hdi/americas/
    - For title containing North Korea and China, we used China HDI

### Date: 2023-02-24

1. Added 2021 SJR metric for all titles. Using this as a
   control
1. Basic data cleanup
1. Renamed main data file to **titlesMain**
1. Keeping the following variables in **titlesMain**:
  - **Citations:** citation counts for each article
  - **SJR:** SJR metric for each article's journal
  - **Publication:** Publication title for each article
  - **Titles:** Title of article
  - **nation:** Name of locality if in title; else **NA**
  - **HDI:** Human Development Index for **nation**
  - **Country/Region:** Binary variable, **C** represents
    country; **R** represents region
  - **averaged:** if multiple countries/regions appeared in
    the title, then the HDI was averaged. This variable
    simply marks that as **Y/N**.
1. Analysis will be based on the following question: do
articles with place names in titles receive fewer citations
compared to articles without place names in titles?

### Date: 2023-02-17

1. Jan 18: Sean used Python script to extract place names
   from titles
   - file: **data/titles-with-places.csv**
1. Jan 30: Anwar reviewed data and checked place names in
   titles
   - file: **data/titles-with-places-Anwar.csv**
1. Feb 17: Sean added 2021 HDI column to data, for each place name
   - file: **data/titles-hdi-citations.csv**
   - original data file: **data/HDR21-22_Statistical_Annex_HDI_Table.xlsx** from [HDI: UNDP][hdiundp]
   - If multiple places in title, HDI was **averaged**
   - United Kingdom HDI was used for Britian or England
   - Region HDI for 'Europe and Central Asia' was picked for
     locations like EU or Europe
   - Region HDI for 'Africa' was picked for locations like
     Africa
   - Nation HDI was used for places that were captured that
     were within nations, like Grenada -> Spain
   - One data point included Tawain plus four other nations.
     We left Tawain out of the average of these since Tawain
     does not have an HDI.
   - One data had 'Iberian'. We averaged Spain and Portugal.
   - Used 'Serbia' for titles containing 'Kosovo',
     recognizing that this is debated, but there is no HDI
     for Kosovo at the time of data collection
   - We used 'Russian Federation' for title containing
     'Soviet Union'
   - One title included both 'North Korea' and 'China'. NK
     does not have an HDI. We only used China.
   - Two titles included 'North Korea' only. We left these
     empty since NK does not have an HDI.
   - Any title containing 'Ireland', we used the HDI for the
     Republic of Ireland.
   - Any title containing 'Scotland', use used the HDI for
     'United Kingdom'
   - We used the U.S. HDI for Puerto Rico

[hdiundp]:https://hdr.undp.org/data-center/human-development-index#/indicies/HDI

### Date: 2023-01-17

1. ~~Titles and citation columns were saved separately.~~
1. ~~Python script used to extract place/country names from
   journal titles.~~
1. ~~Next step -- review place/name extractions for false
   positives.~~
1. ~~Next step -- review for false negatives.~~
1. ~~Add HDI variable for each country name.~~
1. ~~Add SJR for journals for each journal title to control
   for overall impact~~

### Date: 2022-10-02

I combined all 61 downloaded
bib files into one
with the command below, and
saved that in this repo's
data directory:

```
ls -v *bib | xargs cat > ~/lisjournals.bib
mv ~/lisjournals.bib ~/workspace/lisjournals/
```

> Created a new repo called geo-titles and moved data there
> and deleted cseanburns/lisjournals

### Date: 2022-09-14

1. 2021 Scimago data was downloaded on 2022-09-14 from
   https://www.scimagojr.com/journalrank.php?category=3309&area=3300&type=j
   This data is used to identify journals for the study. We selected the following ranking parameters:
   - Social Sciences >
   - Library and Information Sciences >
   - All regions / countries >
   - All types >
   - 2021
1. Scopus data for all 61 journals in the Q1 Scimago ranking were downloaded on
   2022-09-14.
1. I downloaded the **article type** from each journal for issues that were
   published in 2020, 2019, and 2018.
   - Search for journal title using *Scopus* **SRCTITLE** field and limit
     results to 2020, 2019, and 2018 and article type.
   - For example:

   ```
   SRCTITLE ( "International Journal of Information Management" )  AND  (
   LIMIT-TO ( PUBYEAR ,  2020 )  OR  LIMIT-TO ( PUBYEAR ,  2019 )  OR  LIMIT-TO
   ( PUBYEAR ,  2018 ) )  AND  ( LIMIT-TO ( DOCTYPE ,  "ar" ) )
   ```

1. Save data using syntax: **rank#-journalname.bib**. For example, the
   *International Journal of Information Management* is ranked one in Scimago
   and thus the data file is saved as **1-ijinfomgt.bib**.
1. The data is saved as read-only in the **data/** directory.
1. All .bib files were joined into a single file and pulled
   into R using the ``bibliometrix`` package.
1. Before downloading, all data fields were confirmed to be correct. E.g., some
   searches returned results for similar named journals. These were corrected
   before downloading.

[Main Default Data:][datafields]

| Field Tag   | Description                    |
| ----------- | -------------                  |
| AU          | Author                         |
| C1          | Author Address                 |
| AR          | Article Number                 |
| RP          | Reprint Address                |
| DT          | Document Type                  |
| DI          | Digital Object Identifer (DOI) |
| SO          | Publication Name               |
| LA          | Language                       |
| TC          | Times Cited                    |
| DB          | Database                       |
| TI          | Document Title                 |
| VL          | Volume                         |
| PY          | Year Published                 |

[datafields]:http://www.bibliometrix.org/documents/Field_Tags_bibliometrix.pdf

## Data and Meeting notes

### Date: 2022-08-31

**Note:** Based on initial discussions.
We elected to take a different route
after additional discussions
(Mon Oct  9 11:02:13 PM EDT 2023).

Method:

1. Identify journals in the first quartile (Q1) of 2021 Scimago
   LIS journal rankings
2. Sean will download, clean, and save data in a spreadsheet
   file.
   - download *article types* for years 2020, 2019, and 2018
3. Anwar and Sean will meet to discuss coding journal titles
  - Anwar and Sean will code the data as discussed
4. Sean will add HDI for corresponding author's institutional
   affiliation country

Research Question: Is there a geographic bias against
articles with place names in titles

Hypotheses:

1. Articles with place names in the article titles receive
   fewer citations than articles without places names.
2. Articles with place names in the article titles will
   receive more citations if the articles are published by
   corresponding authors from countries with higher HDIs
   than from countries from lower HDIs

- Dependent variable:
  - citations counts of research articles (exclude letters,
    editorials, etc.)
- Independent variables:
  - Country name in title (yes/no)
  - HDI of country name in title
    - if more than one country name, take the average HDI
      [https://hdr.undp.org/data-center/human-development-index#/indicies/HDI][hdi]
  - HDI of corresponding author's institutional affiliation
    country
    - alternatively, take the average HDI for all author
      country affiliations??
  - total docs (2021) from Scimago or the number of documents published in the
    years 2018, 2019, and 2020 since frequency may influence
    visibility
  - total authors, since more authors generally mean more
    citations
  - open access status (yes/no) to account for the OA
    citation advantange

**Regression equation:**

Citation Counts =  
  Country name in title (yes/no) +  
  HDI of country name in title +  
  HDI of corresponding author's institutional affiliation country +  
  total docs (2021) +  
  total authors per article +  
  open access (yes/no)

## Scopus Data

Export all **Citation information**:

- Author(s)
- Author(s) ID
- Document title
- Year
- EID
- Source title
- volume, issue, pages
- Citation count
- Source and document type
- Publication Stage
- DOI
- Open Access

Export the following **Bibliographical information**

- Affiliations
- Language of original document
- Correspondence address

### R

Use the [bibliometrix][bibliometrix] package to help with
analysis.

[bibliometrix]:https://www.bibliometrix.org/home/
[hdi]:https://hdr.undp.org/data-center/human-development-index#/indicies/HDI


