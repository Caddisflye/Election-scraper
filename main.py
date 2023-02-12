import requests
from bs4 import BeautifulSoup
import csv
import sys


def scrape_data(url, file_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all("td")
            link = cells[0].find("a")["href"]
            okrsek_page = requests.get(link)
            okrsek_soup = BeautifulSoup(okrsek_page.content, 'html.parser')
            okrsek_tables = okrsek_soup.find_all('table')


# TODO collect the data from second degree table to a dictionary

# TODO export the dictionary into provided file name


"""
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            data = [cell.text.strip() for cell in row.find_all('td')]
            writer.writerow(data)
"""

# TODO validate that 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj= is in provided website
try:
    url = sys.argv[1]
except:
    url = input("Enter the URL of the website: ")

# TODO validate that '.csv' is in provided file name
try:
    file_name = sys.argv[2]
except:
    file_name = input("Enter the name of the output file: ")

scrape_data(url, file_name)
