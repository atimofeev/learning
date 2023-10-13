"""This code scrapes Wiki page table and prints list of countries with their capitals"""
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_national_capitals"
HCITY_COL = "City/Town"
HCOUNTRY_COL = "Country/Territory"

page = requests.get(URL, timeout=10)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable sortable'})

headers = []
for th in table.find('tr').find_all('th'):
    headers.append(th.text.strip())

country_col = headers.index(HCOUNTRY_COL)
capital_col = headers.index(HCITY_COL)

rows = table.find_all('tr')[1:]

data = []
last_country = ''
for row in rows:
    cols = [col.text.strip() for col in row.find_all('td')]
    if not cols: continue

    capital = cols[capital_col]

    try:
        country = cols[country_col] if cols[country_col] else last_country
    except IndexError:
        country = last_country

    last_country = country
    data.append({'Country': country, 'Capital': capital})

keys = data[0].keys()
with open('countries_and_capitals.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
