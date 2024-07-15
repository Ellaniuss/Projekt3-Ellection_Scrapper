from bs4 import BeautifulSoup as bs
import requests
import csv



url = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xnumnuts=7103"
response = requests.get(url)
soup = bs(response.text, 'html.parser')

tables = soup.find_all('table')
parties = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        cell_name = row.find('td', class_='overflow_name')
        if cell_name:
            party_name = cell_name.text.strip()
            parties.append(party_name)


with open('parties.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(parties)


