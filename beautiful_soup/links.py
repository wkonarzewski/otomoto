from urllib import request
from bs4 import BeautifulSoup as BS
import re


def get_pages_links():
    '''
    creating a list of links to all pages with OPEL ASTRA offers
    '''
    url = "https://www.otomoto.pl/osobowe/opel/astra/?search%5Border%5D=created_at%3Adesc&page=" # base part of url to every page with offers looks the same, only the number of the page at the end changes
    first_url = url + "1"
    html = request.urlopen(first_url)
    bs = BS(html.read(), 'html.parser')
    last_page = int(bs.find_all('a', {'href':re.compile('https:\/\/www.otomoto\.pl/osobowe\/opel\/astra\/\?search%5Border%5D=created_at%3Adesc&page=[0-9]{1,3}')})[-2].span.text)
    print(last_page)
    print('Creating list of links to all pages: IN PROGRESS...')
    start_urls = [url+str(i) for i in range(1,last_page+1)] # creating a list of urls of all pages
    print('Creating list of links to all pages: DONE')
    return start_urls

def get_offer_links(urls, only_100=True):
    '''
    creating a list of links to all OPEL ASTRA offers
    if only_100 is set to True only links to first 100 offers will be scraped
    '''
    offer_links = [] # empty result list
    print('Creating list of links to all offers: IN PROGRESS...')
    for url in urls: # iterating over links to pages scraped by get_pages_links() function
        html = request.urlopen(url)
        bs = BS(html.read(), 'html.parser')
        chunks = bs.find_all('a', {'class':'offer-title__link'}) # creating list of html chunks where links are stored
        for x in chunks: 
            offer_links.append(x['href']) # retrieving links to offers and appending to result list
            if only_100 and len(offer_links) == 100:
                print('Creating list of links to first 100 offers: DONE')
                return offer_links
    print('Creating list of links to all offers: DONE')
    return offer_links
