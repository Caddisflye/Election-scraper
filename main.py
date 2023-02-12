import requests
from bs4 import BeautifulSoup
import csv


def scrape_data(url, file_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            print(row)
"""
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            data = [cell.text.strip() for cell in row.find_all('td')]
            writer.writerow(data)
"""

url = input("Enter the URL of the website: ")
file_name = input("Enter the name of the output file: ")
scrape_data(url, file_name)
