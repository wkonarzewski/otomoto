# this file's task is to scrap data from OPEL ASTRA offers such as mileage, color, price etc.
import scrapy
import re

# boolean parameter: True - scrap only 100 offers, False - scrap all offers
only_100 = True

# this spider scrapes 24 fields, 23 are visible on the website and the 24th is url (in order to be able to go fast to any offer in case of an error)
class Offer(scrapy.Item):
    url = scrapy.Field() # link to offer
    source = scrapy.Field() # private person/company
    category = scrapy.Field() # passenger car/van
    brand = scrapy.Field() # car brand
    model = scrapy.Field() #car model
    generation = scrapy.Field() # car generation
    year = scrapy.Field() # production year
    mileage = scrapy.Field() # current car mileage
    capacity = scrapy.Field() # engine capacity
    fuel = scrapy.Field() # fuel type
    horse_power = scrapy.Field() # engine power
    transmission = scrapy.Field() # gearbox type
    drive = scrapy.Field() # drive type
    type = scrapy.Field() # compact/sedan/kombi/...
    doors = scrapy.Field() # number of doors
    seats = scrapy.Field() # number of seats
    color = scrapy.Field() # car color
    origin = scrapy.Field() # origin country
    first_owner = scrapy.Field() # first owner: yes/no
    not_crashed = scrapy.Field() # never crashed: yes/no
    aso_service = scrapy.Field() # serviced in dealership service
    used = scrapy.Field() # used/new
    price = scrapy.Field() # offer price
    currency = scrapy.Field() # offer currency

class LinksSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['https://www.otomoto.pl/']
    try:
        with open("offer_links.csv", "rt") as f: # opening .csv file created proviously by spider 'offers'
            if only_100:
                start_urls = [url.strip() for url in f.readlines()][1:102] # scraping only 100 offers
            else:
                start_urls = [url.strip() for url in f.readlines()][1:] # scraping all offers
    except:
        start_urls = []

    def parse(self, response):
        o = Offer() 

        # xpaths to all fields
        source_xpath = '//span[text()="Oferta od"]/following-sibling::*/a/@title'
        category_xpath = '//span[text()="Kategoria"]/following-sibling::*/a/@title'
        brand_xpath = '//span[text()="Marka pojazdu"]/following-sibling::*/a/@title'
        model_xpath = '//span[text()="Model pojazdu"]/following-sibling::*/a/@title'
        generation_xpath = '//span[text()="Generacja"]/following-sibling::*/a/@title'
        year_xpath = '//span[text()="Rok produkcji"]/following-sibling::*/text()'
        mileage_xpath = '//span[text()="Przebieg"]/following-sibling::*/text()'
        capacity_xpath = '//span[text()="Pojemność skokowa"]/following-sibling::*/text()'
        fuel_xpath = '//span[text()="Rodzaj paliwa"]/following-sibling::*/a/@title'
        horse_power_xpath = '//span[text()="Moc"]/following-sibling::*/text()'
        transmission_xpath = '//span[text()="Skrzynia biegów"]/following-sibling::*/a/@title'
        drive_xpath = '//span[text()="Napęd"]/following-sibling::*/a/@title'
        type_xpath = '//span[text()="Typ"]/following-sibling::*/a/@title'
        doors_xpath = '//span[text()="Liczba drzwi"]/following-sibling::*/text()'
        seats_xpath = '//span[text()="Liczba miejsc"]/following-sibling::*/text()'
        color_xpath = '//span[text()="Kolor"]/following-sibling::*/a/@title'
        origin_xpath = '//span[text()="Kraj pochodzenia"]/following-sibling::*/a/@title'
        first_owner_xpath = '//span[text()="Pierwszy właściciel"]/following-sibling::*/a/@title'
        not_crashed_xpath = '//span[text()="Bezwypadkowy"]/following-sibling::*/a/@title'
        aso_service_xpath = '//span[text()="Serwisowany w ASO"]/following-sibling::*/a/@title'
        used_xpath = '//span[text()="Stan"]/following-sibling::*/a/@title'
        price_xpath = '//div[@class="offer-price"]/@data-price'
        currency_xpath = '//span[@class="offer-price__currency"]/text()'

        # extracting and transforming data
        o['url'] = response.request.url
        o['source'] = response.xpath(source_xpath).getall()
        o['category'] = response.xpath(category_xpath).getall()
        o['brand'] = response.xpath(brand_xpath).getall()
        try:
            o['model'] = response.xpath(model_xpath).getall()[0].replace("Osobowe ","") # replacing 'Osobowe Astra' with 'Astra'
        except IndexError:
            o['model'] = ""
        o['generation'] = response.xpath(generation_xpath).getall()
        try:
            o['year'] = int(response.xpath(year_xpath).getall()[0])
        except IndexError:
            o['year'] = ""
        try:
            o['mileage'] = int(re.sub("[^0-9]","",response.xpath(mileage_xpath).getall()[0])) # changing for example '158 000 km' to '158000'
        except IndexError:
            o['mileage'] = ""
        try:
            o['capacity'] = round(int(re.sub("[^0-9]","",response.xpath(capacity_xpath).getall()[0]))/10000,1) # changing for example '1 364 cm3' to '1.4'
        except IndexError:
            o['capacity'] = ""
        o['fuel'] = response.xpath(fuel_xpath).getall()
        try:
            o['horse_power'] = int(re.sub("[^0-9]","",response.xpath(horse_power_xpath).getall()[0])) # changing for example '140 KM' to '140'
        except IndexError:
            o['horse_power'] = ""
        o['transmission'] = response.xpath(transmission_xpath).getall()
        o['drive'] = response.xpath(drive_xpath).getall()
        o['type'] = response.xpath(type_xpath).getall()
        try:
            o['doors'] = int(response.xpath(doors_xpath).getall()[0])
        except IndexError:
            o['doors'] = ""
        try:
            o['seats'] = int(response.xpath(seats_xpath).getall()[0])
        except IndexError:
            o['seats'] = ""
        o['color'] = response.xpath(color_xpath).getall()
        o['origin'] = response.xpath(origin_xpath).getall()
        o['first_owner'] = response.xpath(first_owner_xpath).getall()
        o['not_crashed'] = response.xpath(not_crashed_xpath).getall()
        o['aso_service'] = response.xpath(aso_service_xpath).getall()
        o['used'] = response.xpath(used_xpath).getall()
        try:
            o['price'] = int(re.sub("[^0-9]","",response.xpath(price_xpath).getall()[0])) # changing for example '42 900' to '42900'
        except IndexError:
            o['price'] = ""
        try:
            o['currency'] = response.xpath(currency_xpath).getall()[0]
        except IndexError:
            o['currency'] = ""

        yield o
        
