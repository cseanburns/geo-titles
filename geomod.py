import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

titles = pd.read_csv('titles.csv', header = 0, names = ['Citations', 'Titles'], index_col = False)
titles['Titles'] = titles['Titles'].astype(str).str.lower()
titles['Nation'] = [s if (s:=''.join([ent.text for ent in nlp(i).ents])) else 'NA'
                  for i in titles['Titles']]  

---
 
# this is kind of it but not totally:  -->

# here I get the country names
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Mexico']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
for i in data['Text']:
  doc = nlp(i)
  for ent in doc.ents:
    print(ent.text)

# <-- that is it! 

# Got help from StackOverflow
# https://stackoverflow.com/questions/75091694/python-create-column-in-pandas-data-frame-that-matches-row-for-row-values-found
data = [[10, 'I live in America'], [20, 'You ate a cookie'], [30, 'He went to Mexico']]
data = pd.DataFrame(data, columns = ['Numbers', 'Text'])
data['Text'] = data['Text'].astype(str).str.lower()
data['Nation'] = [s if (s:=''.join([ent.text for ent in nlp(i).ents])) else 'NA'
                  for i in data['Text']]  

# alternate from stack overflow
import pycountry
data = [[10, 'I went to Mexico'], [20, 'He ate a sandwich'], [30, 'I went to Canada']]
df = pd.DataFrame(data=data, columns=['Numbers', 'Text'])
countries = [x.name for x in pycountry.countries]
df["Nation"] = df["Text"].str.split(" ").apply(lambda x: ",".join([i for i in x if i in countries])).replace("", "NA")
print(df)
    
#######

doc = nlp(titles.Titles[2060].lower())
for ent in doc.ents:
    print(ent.text)
 
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
  
 
