import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_Ireland'

page = requests.get(url)

soup =BeautifulSoup(page.text, 'html')
                                                                    #get list of row data to convert into df
table = soup.find_all('table')[1]                                   # table[1] to get 2nd table on page
#print(table[1])

column_name= table.find_all('th')                                   #th to get column names
column= [i.text.strip() for i in column_name]                       # strip to remove '/n'
print(column)

df= pd.DataFrame(columns= column)
print(df)

raw= table.find_all('tr')
#print(raw)
for row in raw[1:]:                                                #removing empty row by raw[1:]
    line_row= row.find_all('td')                                   #td to get row values
    row_data=  [line.text.strip() for line in line_row]
    print(row_data)
    length= len(df)
    df.loc[length]= row_data
    
    
#printing df    
print(df)

#converting to csv
df.to_csv('countries.csv',index=False)