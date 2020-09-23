import pandas as pd
import re
pd.set_option("display.max_columns", 3)


# ERROR: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>
# Solution if you are on OSX and Python 3.6: https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
inflation_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_inflation_rate')

print(f'Total tables: {len(inflation_tables)}')

# Preview of tables to scrape
for i in range(len(inflation_tables)):
  print(inflation_tables[i].head())

# create df with the selected table
df = inflation_tables[2]
print(df.head())

# check df shape
print(df.shape)

# check df types
print(df.info())

# set Inflation Rate column to float
infl_rate = []
for i in df['Inflation rate (consumer prices) (%)']:
    if '−' in i:
        i = i.replace('−', '-')
    if '-' in i:
        i = i.replace('-', '-')
    i = float(i)
    infl_rate.append(i)

df['Inflation rate (consumer prices) (%)'] = infl_rate


# remove letters from the Date of Information column
years = []
for i in df['Date of information']:
    i = re.split(' est.', i)[0]
    i = re.sub('\D', '', i)
    years.append(i)

df['Date of information'] = years


# print the 10 highest and lowest inflation rates
df = df.sort_values(by=['Inflation rate (consumer prices) (%)'])
lowest = df.head(10)
highest = df.tail(10)

print(lowest)
print(highest)
