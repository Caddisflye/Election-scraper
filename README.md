# Election scraper
2017 Czech Parliament election website scraper

## Description

This script scrapes election data for any territorial unit from this [website](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). 
The user chooses a specific territory and provides the URL in the "Výběr obce" column of that territory.

## Website

The website URL is provided as the first argument when calling the script from terminal. 
When no URL is provided, the user is asked to provide one.
### Example of the URL for Brno-venkov: 
"https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203"

## Export file

The scraped data will be exported as a .csv file.
The name of the output file needs to be specified as the second argument when calling the script.
When no file name is provided, the user is asked to provide one.
Example of the file name: brno_venkov.csv

## Necessary libraries

requests, beautifulsoup4

## Example

Example of the script call with provided arguments:
```
python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" brno_venkov.csv
```

## Example output

![Imgur](https://imgur.com/Vn51b90.png)