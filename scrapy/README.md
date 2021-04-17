# Scraping Opel Astra offers from otomoto.pl with SCRAPY
\
Go to spiders directory:\
```cd cars/cars/spiders/```\
\
There are two spiders:  

- offers - this spider scrapes links to all OPEL ASTRA offers currently avaliable\
By default only first 100 links will be scraped. In order to scrap all links set parameter ```only_100``` to ```False``` in the 8th line of ```links_offers.py``` file.  
How to run:\
```scrapy crawl offers -o offer_links.csv```  

- cars - this spider scrapes data from all links gathered by ```offers``` spider\
By default data from first 100 links will be scraped. In order to scrap data from all links set parameter ```only_100``` to ```False``` in the 6th line of ```offers_data.py``` file.  
How to run:\
```scrapy crawl cars -o cars_data.csv```  
