# WebDevProject
## How to run Program
1. go into classscraper directory
2. run scrapy crawl classspider
 - Here is the tutorial I followed for Scrapy: https://www.youtube.com/watch?v=mBoX_JCKZTE&t=2983s

## Dependencies
Python 3.11.4
pip 23.1.2
ipython 8.21.0
Scrapy 2.11.0

## Feature Implimentation
Web Crawler
1. Goes to https://catalog.wsu.edu/Pullman/Courses/ to extract all available majors in the catalog
2. Creates list of majors - removes whitespace and duplicates and invalid majors
3. visits each page by iterating through the list of majors

Web Scraper
1. Once the web crawler arrives at a new page, the scraper scrapes the name and description of each class within the major - removes whitespace

### Working features
Web Crawler - Goes through each major in WSU catalog
Web Scraper - On a major page, it extracts the class name and description

### To do:
#### Backend
* parse class name and description so we know: class #, Prerequisites and Class Description
* Save output data into some type of file format to easily export to a mySQL database
* Export data into database
* Build website that pulls from database based on input options
* Build another web crawler/scraper that will download all .csv file that contains additional infromation for each class

#### Frontend
* Build a nice looking website that can show class dependency and class schedule