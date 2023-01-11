import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from geotext import GeoText
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from shapely.geometry import Point, Polygon
import descartes

import spacy

titles = pd.read_csv('titles.csv', header = 0, names = ['Citations', 'Titles'], index_col = False)

nlp = spacy.load("en_core_web_sm")
   
# for i in range(len(titles)):
#   doc = nlp(titles.Titles[i].lower())
  
doc = nlp(titles.Titles[2060].lower())
for ent in doc.ents:
    print(ent.text)
 
---

# testing:

data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Georgia']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
doc = nlp(data.Text[2])
for ent in doc.ents:
  print(ent.text)


doc = nlp(data.Text[0])

data['Countries'] = data['Text'].apply(nlp)


data.Text = nlp(data.Text)
for v in data.Text:
  doc = nlp(v)
 
 
 

 
data = [10,20,30,40,50]
data = pd.DataFrame(data, columns = ['Numbers'])
for v in data['Numbers']:
  print(v)

data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Georgia']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
for v in data['Text']:
  print(v)
  
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Georgia']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
for v in data['Text']:
  data['Country'] = nlp(v.lower())
  
for i in data['Numbers']:
  data['Times2'] = i * 2
  
 
