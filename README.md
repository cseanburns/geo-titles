# geo-titles

## Data notes

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

### Date: 2023-02-17

1. Jan 18: Sean used Python script to extract place names
   from titles
   - file: **data/titles-with-places.csv**
1. Jan 30: Anwar reviewed data and checked place names in
   titles
   - file: **data/titles-with-places-Anwar.csv**
1. Feb 17: Sean added HDI column to data, for each place
   name
  - file: **data/titles-hdi-citations.csv**
  - If multiple places in title, HDI was averaged
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

### Date: 2023-01-17

1. ~~Titles and citation columns were saved separately.~~
1. ~~Python script used to extract place/country names from
   journal titles.~~
1. Next step -- review place/name extractions for false
   positives.
1. Next step -- sample data for false negatives.
1. ~~Add HDI variable for each country name.~~
1. Add JIF for journals for each title to control for
   overall impact
