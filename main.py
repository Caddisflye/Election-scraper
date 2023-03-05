"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Jiri Steif
email: jiristeif (zavinac) seznam.cz
discord: Caddi#3130
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys


def get_tables_from_website(url):
    """
    returns all the tables from specified url website
    :param url: link from which all the tables are to be returned
    :return: all the tables found via the url
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all('table')


def scrape_data(url, file_name):
    """
    :param url: an url for a specific 'Okres'. Must include the part 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj='
    :param file_name: name of the final file where data will be exported
    :return: nothing
    """
    tables = get_tables_from_website(url)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ["code",
                  "location",
                  "registered",
                  "envelopes",
                  "valid",
                  "Občanská demokratická strana",
                  "Řád národa - Vlastenecká unie",
                  "CESTA ODPOVĚDNÉ SPOLEČNOSTI",
                  "Česká str.sociálně demokrat.",
                  "Radostné Česko",
                  "STAROSTOVÉ A NEZÁVISLÍ",
                  "Komunistická str.Čech a Moravy",
                  "Strana zelených",
                  "ROZUMNÍ-stop migraci,diktát.EU",
                  "Strana svobodných občanů",
                  "Blok proti islam.-Obran.domova",
                  "Občanská demokratická aliance",
                  "Česká pirátská strana",
                  "Referendum o Evropské unii",
                  "TOP 09",
                  "ANO 2011",
                  "Dobrá volba 2016",
                  "SPR-Republ.str.Čsl. M.Sládka",
                  "Křesť.demokr.unie-Čs.str.lid.",
                  "Česká strana národně sociální",
                  "REALISTÉ",
                  "SPORTOVCI",
                  "Dělnic.str.sociální spravedl.",
                  "Svob.a př.dem.-T.Okamura (SPD)",
                  "Strana Práv Občanů"
                  ]  # manually written header row
        writer.writerow(header)
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all("td")
                if cells and cells[0].find("a"):
                    # the link in the tables is not absolute,so adding the necessary part
                    link = "https://www.volby.cz/pls/ps2017nss/" + cells[0].find("a")["href"]
                    data = [cells[0].find("a").get_text(), cells[1].get_text()]  # code column

                    # using the found link in the "číslo" column to get to the tables with values to export
                    okrsek_tables = get_tables_from_website(link)

                    # getting values from the first summary table
                    okrsek_souhrn_table = okrsek_tables[0]
                    okrsek_souhrn_row = okrsek_souhrn_table.find_all("tr")[2]
                    okrsek_souhrn_cells = okrsek_souhrn_row.find_all("td")
                    data.append(okrsek_souhrn_cells[3].get_text())  # registered column
                    data.append(okrsek_souhrn_cells[4].get_text())  # envelopes column
                    data.append(okrsek_souhrn_cells[7].get_text())  # valid column

                    # getting values from the second and third tables containing values for specific political parties
                    for i in range(1, 3):
                        okrsek_strany_rows = okrsek_tables[i].find_all("tr")
                        for okrsek_strany_row in okrsek_strany_rows:
                            okrsek_strany_cells = okrsek_strany_row.find_all("td")
                            if okrsek_strany_cells:
                                okrsek_strany_value = okrsek_strany_cells[2].get_text()
                                if okrsek_strany_value.isnumeric():
                                    data.append(okrsek_strany_value)

                    writer.writerow(data)


if __name__ == "__main__":
    try:
        website = sys.argv[1]
    except:
        website = input("Enter the URL of the website: ")

    # check for the necessary part of the website for the code to work
    if "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" not in website:
        print("Incorrect website url.")
        print("Please provide a website including 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj='")
        quit()

    try:
        provided_file_name = sys.argv[2]
    except:
        provided_file_name = input("Enter the name of the output file: ")

    scrape_data(website, provided_file_name)
