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
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
    return soup.find_all('table')


def save_to_csv(file_name, header, csv_data):
    """
    Write the scraped data into file
    :param file_name: path where the data will be exported to
    :param header: header of the csv file
    :param csv_data: scraped data
    """
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(csv_data)


def check_input_website():
    """
    Check the existence of the website to scrape, if none is found, or incorrect website is provided, ask user for new
    :return: website to be scraped
    """
    try:
        link = sys.argv[1]
    except:
        link = input("Enter the URL of the website: ")

    # check for the necessary part of the website for the code to work
    if "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" not in link:
        print("Incorrect website url.")
        print("Please provide a website including 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj='")
        quit()

    return link


def check_input_file():
    """
    Check the existence of the file name as an argument, if none is found, ask for it
    :return: name of the file where data will be exported
    """
    try:
        file_name = sys.argv[2]
    except:
        file_name = input("Enter the name of the output file: ")

    return file_name


def get_row_data(cells, header):
    """
    This function returns updated header variable and all necessary columns for a single row of the final csv file.
    :param cells:
    :param header:
    :return: data - list of values for each column, header - updated variable with additional political parties
    """
    # the link in the tables is not absolute,so adding the necessary part
    link = "https://www.volby.cz/pls/ps2017nss/" + cells[0].find("a")["href"]

    data = [cells[0].find("a").get_text(), cells[1].get_text()]  # code column

    # using the found link in the "číslo" column to get to the tables with values to export
    okrsek_tables = get_tables_from_website(link)

    # getting values from the first summary table
    okrsek_souhrn_cells = okrsek_tables[0].find_all("tr")[2].find_all("td")
    data.append(okrsek_souhrn_cells[3].get_text())  # registered column
    data.append(okrsek_souhrn_cells[4].get_text())  # envelopes column
    data.append(okrsek_souhrn_cells[7].get_text())  # valid column

    # getting values from the second and third tables containing values for specific political parties
    for i in range(1, 3):
        okrsek_strany_rows = okrsek_tables[i].find_all("tr")
        for okrsek_strany_row in okrsek_strany_rows:
            okrsek_strany_cells = okrsek_strany_row.find_all("td")
            if okrsek_strany_cells:  # check if not a row of empty cells
                strana = okrsek_strany_cells[1].get_text()
                okrsek_strany_value = okrsek_strany_cells[2].get_text()
                data.append(okrsek_strany_value)

                # if strana not in header -> append it
                if strana not in header:
                    header.append(strana)

    return data, header


def scrape_data(url):
    """
    :param url: an url for a specific 'Okres'. Must include the part 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj='
    :return: list of elements: header, csv_data
    """
    tables = get_tables_from_website(url)
    csv_data = []
    header = ["code", "location", "registered", "envelopes", "valid"]  # manually written start of the header row

    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all("td")
            if cells and cells[0].find("a"):  # check if not an empty cell

                data, header = get_row_data(cells, header)

                csv_data.append(data)

    return [header, csv_data]


def main():
    """
    main function of the script
    """
    website = check_input_website()
    provided_file_name = check_input_file()
    data = scrape_data(website)
    save_to_csv(provided_file_name, data[0], data[1])


if __name__ == "__main__":

    main()
