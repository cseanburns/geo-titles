# This code extracts place names from the journal article titles. There are a
# lot of false positives. Need to remove those and then sample for false
# negatives.

# Date: 2023-01-18

import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

# Read and prep data
titles = pd.read_csv('data/titles.csv', header = None, names = ['Citations', 'Titles'], index_col = False)
titles['Titles'] = titles['Titles'].astype(str).str.lower()

# Locate data with place names
titles['Nation'] = [s if (s:=''.join([ent.text for ent in nlp(i).ents])) else 'NA'
                  for i in titles['Titles']]  

# Export data
titles.to_csv("data/titles-with-places.csv", index=True)

# Recieved some tips on the above script from:
# https://stackoverflow.com/questions/75091694/python-create-column-in-pandas-data-frame-that-matches-row-for-row-values-found

# Note: after extracting place names with above script,
# @anwar checked data and added NA in empty cells for titles with no place names

# With help from OpenAI ChatGPT 3.5:
# Locates the position of the named entity in the text

def find_places(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            return ent.end_char / len(text)
    return None
  
titles['places'] = titles['Titles'].apply(find_places)

# Export data
titles.to_csv("data/titles-with-place-positions.csv", index=True)

# Try this later, rewrite of the above using the walrus operator:
titles['places'] = [ent.end_char / len(text) if (ent:=next((ent for ent in nlp(i).ents if ent.label_ == 'GPE'), None)) else None for i in titles['Titles']]

