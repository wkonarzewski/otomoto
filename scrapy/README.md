# Scraping Opel Astra offers from otomoto.pl with SCRAPY
\
Create new scrapy project and put both files (```links_offers.py``` and ```offers_data.py```) into spiders directory.


There are two spiders:  

- offers - this spider scrapes links to all OPEL ASTRA offers currently avaliable\
By default links from only first 100 pages will be scraped. In order to scrap all links set parameter ```only_100``` to ```False``` in the 8th line of ```links_offers.py``` file.  
How to run:\
```scrapy crawl offers -o offer_links.csv```


Scraped links can be found in exported ```offer_links.csv``` file.


- cars - this spider scrapes data from all links gathered by ```offers``` spider\
By default data from first 100 links will be scraped. In order to scrap data from all links set parameter ```only_100``` to ```False``` in the 6th line of ```offers_data.py``` file.  
How to run:\
```scrapy crawl cars -o cars_data.csv```


Scraped data can be found in exported ```cars_data.csv``` file.
