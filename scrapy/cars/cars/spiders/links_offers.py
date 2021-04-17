# this file's task is to scrap links to all OPEL ASTRA offer websites
import scrapy
from urllib import request
from bs4 import BeautifulSoup as BS
import re

# boolean parameter: True - scrap only 100 pages, False - scrap all pages
only_100 = True

# base part of url to every page with offers looks the same, only the number of the page at the end changes
url = "https://www.otomoto.pl/osobowe/opel/astra/?search%5Border%5D=created_at%3Adesc&page="

if only_100: #scraping 100 pages
    last_page = 101
else: #scraping all pages
    # Beautifull Soup will be used to get the current number of pages (as it can change every day)
    first_url = url + "1"
    html = request.urlopen(first_url)
    bs = BS(html.read(), 'html.parser')
    last_page = int(bs.find_all('a', {'href':re.compile('https:\/\/www.otomoto\.pl/osobowe\/opel\/astra\/\?search%5Border%5D=created_at%3Adesc&page=[0-9]{1,3}')})[-2].span.text)


class Link(scrapy.Item):
    link = scrapy.Field() # there is only one field thing scraped here from every page (or rather many things of the same kind) - links to offers

class LinksSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['https://www.otomoto.pl/']

    # creating a list of urls of all pages
    start_urls = [url+str(i) for i in range(1,last_page)]

    def parse(self, response):

        # xpath to links to offers (there are up to 32 offers on each page)
        offer_xpath = '//h2[@class="offer-title ds-title"]/a/@href'
        selection = response.xpath(offer_xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l