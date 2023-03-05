# Election scraper
2017 Czech Parliament election data scraper

This script scrapes election data for any territorial unit from this [website](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). 
The user chooses a specific territory and provides the URL in the "Výběr obce" column of that territory.

This URL is provided as the first argument when calling the script from terminal. 
When no URL is provided, the user is asked to provide one.
Example of the URL for Havlíčkův Brod: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6101"

The scraped data will be exported as a .csv file.
The name of the output file needs to be specified as the second argument when calling the script.
When no file name is provided, the user is asked to provide one.
Example of the file name: havlickuv_brod.csv

Necessary libraries: requests, beautifulsoup4

Example of the script call with provided arguments:
```
python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204" zlin.csv
```

Output of this example:

![output_example](https://imgur.com/a/laki3sd)