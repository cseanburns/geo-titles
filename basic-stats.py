import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from flashgeotext.geotext import GeoText

titles = pd.read_csv('titles.csv', header = None)
titles.dtypes
titles.columns
titles.describe()
titles.info()
titles.head()
titles.tail()

# check for equalites
titles.eq(0) # equal: returns true/false for values equal to 0
titles.ne(0) # not equal: returns true/false for values equal to 0

# Examine each column
titles.loc[:,0]
titles.loc[:,1]

# Get mean for column '0'
np.mean(titles[0])
np.median(titles[0])
np.min(titles[0])
np.max(titles[0])
np.max(titles[0]) - np.min(titles[0])
np.std(titles[0])
round(np.std(titles[0]), 3)

# Examine some rows
titles.loc[0]
titles.loc[1]

# Examine rows that meet thresholds
titles.loc[(titles[0] == 0)]
titles.loc[(titles[0] > 100)]
titles.loc[(titles[0] > 1000)]
titles.loc[(titles[0] > 500) & (titles[0] < 900)]
titles.loc[(titles[0] > 1400) & (titles[0] < 1500)]

# Check for null values
titles.isnull().sum()

# Boxplot
pd.DataFrame.boxplot(titles, column = 0)
plt.show()
plt.clf() # clear plot

# Histogram
pd.DataFrame.hist(titles, column = 0)
plt.show()
plt.clf()

# Line plot
titles.plot.line(column = 0)
plt.show()
plt.clf()

geotext = GeoText()
geotext.extract(input_text=titles.iloc[:,1]).item
