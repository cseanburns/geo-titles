import pandas as pd
import spacy

titles = pd.read_csv('titles.csv', header = 0, names = ['Citations', 'Titles'], index_col = False)

nlp = spacy.load("en_core_web_sm")
   
# for i in range(len(titles)):
#   doc = nlp(titles.Titles[i].lower())
  
doc = nlp(titles.Titles[2060].lower())
for ent in doc.ents:
    print(ent.text)
 
---

# this is it:  -->

# here I get the country names
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Mexico']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
for i in data['Text']:
  doc = nlp(i)
  for ent in doc.ents:
    print(ent.text)

# <-- that is it! 

# here I get the country names in a list!
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Mexico']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
countries = []
for i in data['Text']:
  doc = nlp(i)
  for ent in doc.ents:
    countries.append(ent.text)
    
#######

### To do: create a list with Null values where no country is listed
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Georgia']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
countries = []
for i in data['Text']:
  doc = nlp(i)
  for ent in doc.ents:
    countries.append(ent.text)

# trying to create a list from output above and have empty values match
# titles with no country name listed in the title
names = ['soren','inara','','aster']

for i in names:
    if len(i) == 0:
        print("this item is empty")
    else:
        print(i)

    
## playground: learning below

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
  
 
