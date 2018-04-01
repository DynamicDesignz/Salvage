# Salvage

Simple web scraping app written in Python (Scrapy framework), using bash shell to handle configuration files and do basic data manipulation. It scrapes information (prices, mileages, links and more) from one of the car auctioning websites. It doesn't follow the links into each auction, therefore generates only small amount of traffic.


## About Scrapy

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival. Read more [here](https://docs.scrapy.org/).

## Structure

Main script (or as it is called in Scrapy framework, a spider) resides in salvage/spiders directory under the name of salvage.py.
There are two configuration files, but you have to edit only one:

* config - this is the one that you need to edit. It consists of set of key/value pairs - keys are written in English and they shall stay immutable. TYPE, FUEL and BODY values are written in Polish due to the fact that the website we're scraping is a Polish website. Here are the values you can set:


| Key | Value |
| --- | --- |
| TYPE | has to be written in Polish, e.g. osobowe, dostawcze, ciezarowe |
| MAKE | simply any kind of car make, say audi or volkswagen |
| MODEL | this value has to be correct model of a car make you specified above |
| VERSION | format: \<value\>-\<start of production\>-\<end of production\> - first value is the name of the exact model version you want to scrape (say b6 for audi a4, or iv for volkswagen golf), second and third are respectively start and end of this versions' production. They need to match, so you may want to look up these on the Internet |
| ADDITIONAL | additional info, for example the province you want to list (e.g. dolnoslaskie, wielkopolskie) |


Any information given in criteria above will be bonded into a single link in the shell script and then used by the python file.

| Key | Value |
| --- | --- |
| PRICE_MIN | specify the minimal price |
| PRICE_MAX | specify the maximal price |
| FUEL | has to be written in Polish, e.g. Benzyna, Diesel, Benzyna+LPG |
| BODY | has to be written in Polish, e.g. Sedan, Kombi |
| YEAR | specify the year of production. Will list any car matching this year, or younger |

Any information given in criteria above will be read directly from the python file and applied to each result.

## Getting started

## Prerequisites

Before you run the script, you have to install Scrapy. Scrapy runs on Python 2.7 and Python 3.4 or above under CPython (default Python implementation) and PyPy (starting with PyPy 5.9). To install, simply type:
```
pip install Scrapy
```
For more information regarding installation visit [this](https://docs.scrapy.org/en/latest/intro/install.html) site.

## Running the script
To run the script proceed to the main directory of the project and simply type:
```
./scraper.sh
```

Output of the script will be saved into a .csv file, each result taking one row of labeled data. There will be created a directory named after today's date (if it has been already made, no additional directories will be created) and the .csv filename will be labeled with the exact time (hours + minutes) at which it was created.
