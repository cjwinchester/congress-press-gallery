import csv

import requests
from bs4 import BeautifulSoup

url = 'https://www.dailypress.senate.gov/?page_id=67'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table', {'class': 'tablepress'})
rows = table.find_all('tr')

with open('congress-press.csv', 'w') as outfile:

    writer = csv.DictWriter(outfile, fieldnames=['org', 'first', 'last'])
    writer.writeheader()

    for row in rows:
        try:
            if row.find('td').string:
                s = [x.string.strip() for x in row if x.string and x != '\n']
                writer.writerow({
                    'org': s[0],
                    'first': s[1],
                    'last': s[2]
                })
        except AttributeError:
            pass
