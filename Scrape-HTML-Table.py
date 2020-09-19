import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

# Solution if you are on OSX and Python 3.6: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
inflation_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_inflation_rate')

print(f'Total tables: {len(inflation_tables)}')

# Preview of table to scrape
# print(inflation_tables[2])

# create df with the selected table
df = inflation_tables[2]
print(df.head())

# check df types
print(df.info())

# set Inflation Rate column to float


#df['Inflation rate (consumer prices) (%)'] = df['Inflation rate (consumer prices) (%)'].astype('float')


# set Data column to int. Get rid of 'est.'
df['Date of information'] = df['Date of information'].replace({'est.':''}, regex=True).astype('int64')



