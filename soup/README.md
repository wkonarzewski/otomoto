# Scraping Opel Astra offers from otomoto.pl with BEAUTIFUL SOUP

### How does it work:
- searching for number of pages with offers
- creating list of links to all pages
- creating list of links to offers from all pages
- scraping desired data from every offer

### How to run:
```python3 main.py```


By default data from first 100 offers will be scraped. In order to scrap data from all offers set parameter ```only_100``` to ```False``` in the 7th line of ```main.py``` file.


Scraped data can be found in exported ```bs_results.csv``` file.