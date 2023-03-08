# This code extracts place names from the journal article titles. There are a
# lot of false positives. Need to remove those and then sample for false
# negatives.

# Date: 2023-01-18

import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

titles = pd.read_csv('titles.csv', header = 0, names = ['Citations', 'Titles'], index_col = False)
titles['Titles'] = titles['Titles'].astype(str).str.lower()
titles['Nation'] = [s if (s:=''.join([ent.text for ent in nlp(i).ents])) else 'NA'
                  for i in titles['Titles']]  

titles.to_csv("data/titles-with-places.csv", index=True)

# Recieved some tips on the above script from:
# https://stackoverflow.com/questions/75091694/python-create-column-in-pandas-data-frame-that-matches-row-for-row-values-found

# Note: after extracting place names with above script, @anwar checked data and added NA in empty cells for titles with no place names
