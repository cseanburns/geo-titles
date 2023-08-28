#!/usr/bin/python3

# Extract place names in article titles and add names to new colum
# else add NA

import pandas as pd
import spacy
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

title = pd.read_csv('data/titles.csv', header = None, names = ['Citations', 'Titles'], index_col = False)
title['Titles'] = title['Titles'].astype(str).str.lower()

def extract_place_names(title):
    # Process whole documents
    doc = nlp(title)

    # Analyze syntax
    places = [entity.text for entity in doc.ents if entity.label_ == 'GPE']

    if places:
        return ', '.join(places)
    else:
        return 'NA'

title['nation'] = title['Titles'].apply(extract_place_names)

# identify location of place name in column: 0 equals no place name and 1 equals place name at the end

def find_places(text):
    doc = nlp(text)
    positions = []

    for ent in doc.ents:
        if ent.label_ == 'GPE':
            start_pos = (ent.start_char + 1) # start point of the place name
            relative_pos = start_pos / len(text)
            positions.append(relative_pos)

    if not positions:
        return 0
    else:
        # If there are multiple place names, return the average position
        return sum(positions) / len(positions)

title['places'] = title['Titles'].apply(find_places)

# Export data
title.to_csv("data/titles-with-places-testing.csv", index=True)
