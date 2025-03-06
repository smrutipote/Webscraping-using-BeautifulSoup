# Webscraping-using-BeautifulSoup

📌 Wikipedia Web Scraper: Largest Companies in Ireland

📖 Project Overview

This Python project scrapes a Wikipedia page that lists the largest companies in Ireland and saves the extracted data as a CSV file.

🔗 Target URL: Wikipedia - Largest Companies in Ireland

🔧 Features

✅ Scrapes data from Wikipedia using BeautifulSoup✅ Extracts table data including company names, revenues, employees, etc.✅ Cleans and processes the extracted data✅ Converts the data into a pandas DataFrame✅ Saves the data as a CSV file (countries.csv)

🛠️ Setup and Installation

Step 1: Install Required Libraries

Before running the script, install the necessary dependencies:

pip install requests beautifulsoup4 pandas

Step 2: Run the Python Script

python Beautifulsoup_webscraping.py

Step 3: Check the Output

The extracted data will be printed in the terminal

A CSV file countries.csv will be created with the extracted data

📜 Code Explanation

1️⃣ Importing Required Libraries

import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

requests: Fetches the Wikipedia page content

BeautifulSoup: Parses the HTML content

pandas: Stores and processes the extracted data

2️⃣ Fetching the Wikipedia Page

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Ireland'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

Fetches the HTML content from the Wikipedia page

Parses the page using BeautifulSoup

3️⃣ Extracting the Table Data

table = soup.find_all('table')[1]  # Selecting the second table

Wikipedia pages contain multiple tables; the script selects the second table (table[1]).

4️⃣ Extracting Column Headers

column_name = table.find_all('th')
column = [i.text.strip() for i in column_name]  # Strip removes newline characters
print(column)

Extracts column headers from the table and cleans them.

5️⃣ Creating a Pandas DataFrame

df = pd.DataFrame(columns=column)
print(df)

Creates an empty DataFrame with the extracted column headers.

6️⃣ Extracting Row Data

raw = table.find_all('tr')
for row in raw[1:]:  # Skipping the first row to remove empty rows
    line_row = row.find_all('td')
    row_data = [line.text.strip() for line in line_row]
    length = len(df)
    df.loc[length] = row_data

Iterates over the table rows and extracts data cell by cell.

Removes empty rows and appends data to the DataFrame.

7️⃣ Saving Data to CSV File

df.to_csv('countries.csv', index=False)

Saves the scraped data into a CSV file named countries.csv.
