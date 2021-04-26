# Scraping Opel Astra offers from otomoto.pl with SELENIUM


### How does it work:
- open the website
- creating list of links to all pages
- creating list of links to offers from all pages
- scraping desired data from every offer


### Before run the file:
- check your searching engine (ex.Chrome, FireFox...)
- install seleium -- pip install selenium
- download ```chromedriver.exe``` or ```geckodriver.exe```  
- if the exe file is not in bin folder move them into the bin folder 
  -- mv chromedriver.exe /usr/local/bin/chromedriver

 
### How to run:
- open the ```selenium_otomoto.py```
- 18th line in ```selenium_otomoto.py``` might different: for mac (chrome_path = /usr/local/bin/chromedriver)
- 10th line in ```selenium_otomoto.py``` set parameter ```create_csv``` to ```False```, csv will not be created
- run it normally


By default data from first 100 offers will be scraped. In order to scrap data from all offers set parameter ```only_100``` to ```False``` in the 9th line of ```selenium_otomoto.py``` file.


Scraped data can be found in exported ```selenium_results.csv``` file.
