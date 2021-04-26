from selenium import webdriver
import time
import getpass
import datetime
import pandas as pd
from tqdm import tqdm

# if only_100 = True then only scrape 100 pages
only_100 = True
create_csv = True

chrome_path = '/usr/local/bin/chromedriver'

url = 'https://www.otomoto.pl/osobowe/opel/astra/?search%5Border%5D=created_at%3Adesc'

options = webdriver.chrome.options.Options()
options.headless = False

driver = webdriver.Chrome(options = options, executable_path = chrome_path)

# Actual program:
driver.get(url)
time.sleep(3)


# click accept rule 
accept_rule = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
accept_rule.click()
time.sleep(2)


ListOfLinks = []

# collect link from 100 pages
page = 1
while only_100:
    if page <= 100:
        car_links = driver.find_elements_by_class_name('offer-item__content')
        for car_link in car_links:
            car1 = car_link.find_elements_by_tag_name('a')[0]
            ListOfLinks.append(car1.get_property('href'))

        try:
            next_page = driver.find_element_by_class_name('icon-arrow_right')
            next_page.click()
        except:
            condition = False
        page += 1
    else:
        break

# collect link from whole pages
while only_100 == False:
    car_links = driver.find_elements_by_class_name('offer-item__content')
    for car_link in car_links:
        car1 = car_link.find_elements_by_tag_name('a')[0]
        ListOfLinks.append(car1.get_property('href'))

    try:
        next_page = driver.find_element_by_class_name('icon-arrow_right')
        next_page.click()
    except:
        condition = False
    page += 1
     
print("links all collected")

# use the link collected above enter them and collect the informations
# create the list for the information
car_info = [] # create the list for the information
for i in tqdm(ListOfLinks):
    driver.get(i)
    car_data = driver.find_elements_by_class_name('offer-params__item')

    for car in car_data[:1]:


        try:
            Oferta_od = car.find_element_by_xpath('//span[text()="Oferta od"]/following-sibling::*/a').text
        except:
            Oferta_od = ''

        try:
            KategoriaOsobowe = car.find_element_by_xpath('//span[text()="Kategoria"]/following-sibling::*/a').text
        except:
            KategoriaOsobowe = ''

        try:    
            Marka_pojazdu = car.find_element_by_xpath('//span[text()="Marka pojazdu"]/following-sibling::*/a').text
        except:
            Marka_pojazdu = ''

        try:
            Model_pojazdu = car.find_element_by_xpath('//span[text()="Model pojazdu"]/following-sibling::*/a').text
        except:
            Model_pojazdu = ''

        try:
            Generacja = car.find_element_by_xpath('//span[text()="Generacja"]/following-sibling::*/a').text
        except:
            Generacja = ''

        try:
            Rok_produkcji = car.find_element_by_xpath('//span[text()="Rok produkcji"]/following-sibling::*').text
        except:
            Rok_produkcji = ''

        try:
            Przebieg = car.find_element_by_xpath('//span[text()="Przebieg"]/following-sibling::*').text
        except:
            Przebieg = ''

        try:
            Pojemność_skokowa = car.find_element_by_xpath('//span[text()="Pojemność skokowa"]/following-sibling::*').text
        except:
            Pojemność_skokowa = ''

        try:
            Rodzaj_paliwa = car.find_element_by_xpath('//span[text()="Rodzaj paliwa"]/following-sibling::*/a').text
        except:
            Rodzaj_paliwa = ''

        try:
            Moc = car.find_element_by_xpath('//span[text()="Moc"]/following-sibling::*').text
        except:
            Moc = ''

        try:
            Skrzynia_biegów = car.find_element_by_xpath('//span[text()="Skrzynia biegów"]/following-sibling::*/a').text
        except:
            Skrzynia_biegów = ''

        try:
            Napęd = car.find_element_by_xpath('//span[text()="Napęd"]/following-sibling::*/a').text
        except:
            Napęd = ''

        try:
            Typ = car.find_element_by_xpath('//span[text()="Typ"]/following-sibling::*/a').text 
        except:
            Typ = ''

        try:
            Liczba_drzwi = car.find_element_by_xpath('//span[text()="Liczba drzwi"]/following-sibling::*').text 
        except:
            Liczba_drzwi = ''

        try:
            Liczba_miejsc = car.find_element_by_xpath('//span[text()="Liczba miejsc"]/following-sibling::*').text 
        except:
            Liczba_miejsc = ''

        try:
            Kolor = car.find_element_by_xpath('//span[text()="Kolor"]/following-sibling::*/a').text 
        except:
            Kolor = ''

        try:
            Kraj_pochodzenia = car.find_element_by_xpath('//span[text()="Kraj pochodzenia"]/following-sibling::*/a').text   
        except:
            Kraj_pochodzenia = 'Unknown' 

        try:
            pierwszy_właściciel = car.find_element_by_xpath('//span[text()="Pierwszy właściciel"]/following-sibling::*/a').text
        except:
            pierwszy_właściciel = 'Nie'

        try:
            Bezwypadkowy = car.find_element_by_xpath('//span[text()="Bezwypadkowy"]/following-sibling::*/a').text
        except:
            Bezwypadkowy = 'Nie'

        try:
            Serwisowany_w_ASO = car.find_element_by_xpath('//span[text()="Serwisowany w ASO"]/following-sibling::*/a').text
        except:
            Serwisowany_w_ASO = 'Nie'

        try:
            Stan = car.find_element_by_xpath('//span[text()="Stan"]/following-sibling::*/a').text
        except:
            Stan = ''


   
    Cena = driver.find_elements_by_class_name('offer-price__number')
    for price in Cena[:1]:
        try:
            number = price.find_element_by_xpath('//*[@id="siteWrap"]/main/div[1]/div[2]/div[1]/div[1]/div[2]/div/span[1]').text
            A = number[:-3]
            Cena = int(A.replace(' ',''))
        except:
            Cena = ''


    Waluta = driver.find_elements_by_class_name('offer-price__currency')
    for currency in Waluta[:1]:
        try:
            Waluta = currency.find_element_by_xpath('//*[@id="siteWrap"]/main/div[1]/div[2]/div[1]/div[1]/div[2]/div/span[1]/span').text

        except:
            Waluta = ''
 


    car_item = {
                'Cena' : Cena,
                'Waluta' : Waluta,
                'Oferta od': Oferta_od,
                'KategoriaOsobowe': KategoriaOsobowe,
                'Marka pojazdu': Marka_pojazdu,
                'Model pojazdu' : Model_pojazdu,
                'Generacja' : Generacja,
                'Rok produkcji' : Rok_produkcji,
                'Przebieg' : Przebieg,
                'Pojemność skokowa' : Pojemność_skokowa,
                'Rodzaj paliwa' : Rodzaj_paliwa,
                'Moc' : Moc,
                'Skrzynia biegów' : Skrzynia_biegów,
                'Napęd' : Napęd,
                'Typ' : Typ,
                'Liczba drzwi' : Liczba_drzwi,
                'Liczba miejsc' : Liczba_miejsc,
                'Kolor' : Kolor,
                'Kraj pochodzenia' : Kraj_pochodzenia,
                'Pierwszy Właściciel':pierwszy_właściciel,
                'Bezwypadkowy' : Bezwypadkowy,
                'Serwisowany w ASO' : Serwisowany_w_ASO,
                'Stan' : Stan
            }
    car_info.append(car_item)
# use the dataframe 
df = pd.DataFrame(car_info) 

# create the csvfile
if create_csv==True:
    df.to_csv('selenium_results.csv')

print("Scraping data: DONE")
driver.quit()