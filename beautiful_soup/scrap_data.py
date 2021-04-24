from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd


def scrap(offer_links):
    """
    scraping desired fields
    offer_links - list of links
    """
    df = pd.DataFrame(
        {
            "url": [],
            "source": [],
            "category": [],
            "brand": [],
            "model": [],
            "generation": [],
            "year": [],
            "mileage": [],
            "capacity": [],
            "fuel": [],
            "horse_power": [],
            "transmission": [],
            "drive": [],
            "type": [],
            "doors": [],
            "seats": [],
            "color": [],
            "origin": [],
            "first_owner": [],
            "not_crashed": [],
            "aso_service": [],
            "used": [],
            "price": [],
            "currency": [],
        }
    )

    for link in offer_links:
        html = request.urlopen(link)
        bs = BS(html.read(), "html.parser")
        try:
            url = link
        except:
            url = ""
        try:
            source = bs.find("span", string="Oferta od").find_next_sibling().a["title"]
        except:
            source = ""
        try:
            category = (
                bs.find("span", string="Kategoria").find_next_sibling().a["title"]
            )
        except:
            category = ""
        try:
            brand = (
                bs.find("span", string="Marka pojazdu").find_next_sibling().a["title"]
            )
        except:
            brand = ""
        try:
            model = (
                bs.find("span", string="Model pojazdu").find_next_sibling().a["title"]
            ).replace("Osobowe ", "")
        except:
            model = ""
        try:
            generation = (
                bs.find("span", string="Generacja").find_next_sibling().a["title"]
            )
        except:
            generation = ""
        try:
            year = int(bs.find("span", string="Rok produkcji").find_next_sibling().text)
        except:
            year = ""
        try:
            mileage = int(
                re.sub(
                    "[^0-9]",
                    "",
                    bs.find("span", string="Przebieg").find_next_sibling().text,
                )
            )
        except:
            mileage = ""
        try:
            capacity = round(
                int(
                    re.sub(
                        "[^0-9]",
                        "",
                        bs.find("span", string="Pojemność skokowa")
                        .find_next_sibling()
                        .text,
                    )
                )
                / 10000,
                1,
            )

        except:
            capacity = ""
        try:
            fuel = (
                bs.find("span", string="Rodzaj paliwa").find_next_sibling().a["title"]
            )
        except:
            fuel = ""
        try:
            horse_power = int(
                re.sub(
                    "[^0-9]", "", bs.find("span", string="Moc").find_next_sibling().text
                )
            )
        except:
            horse_power = ""
        try:
            transmission = (
                bs.find("span", string="Skrzynia biegów").find_next_sibling().a["title"]
            )
        except:
            transmission = ""
        try:
            drive = bs.find("span", string="Napęd").find_next_sibling().a["title"]
        except:
            drive = ""
        try:
            type = bs.find("span", string="Typ").find_next_sibling().a["title"]
        except:
            type = ""
        try:
            doors = int(bs.find("span", string="Liczba drzwi").find_next_sibling().text)
        except:
            doors = ""
        try:
            seats = int(
                bs.find("span", string="Liczba miejsc").find_next_sibling().text
            )
        except:
            seats = ""
        try:
            color = bs.find("span", string="Kolor").find_next_sibling().a["title"]
        except:
            color = ""
        try:
            origin = (
                bs.find("span", string="Kraj pochodzenia")
                .find_next_sibling()
                .a["title"]
            )
        except:
            origin = ""
        try:
            first_owner = (
                bs.find("span", string="Pierwszy właściciel")
                .find_next_sibling()
                .a["title"]
            )
        except:
            first_owner = ""
        try:
            not_crashed = (
                bs.find("span", string="Bezwypadkowy").find_next_sibling().a["title"]
            )
        except:
            not_crashed = ""
        try:
            aso_service = (
                bs.find("span", string="Serwisowany w ASO")
                .find_next_sibling()
                .a["title"]
            )
        except:
            aso_service = ""
        try:
            used = bs.find("span", string="Stan").find_next_sibling().a["title"]
        except:
            used = ""
        try:
            price = int(
                re.sub("[^0-9]", "", bs.find("div", {"class": "offer-price"})["data-price"])
            )
        except:
            price = ""
        try:
            currency = bs.find("span", {"class": "offer-price__currency"}).text
        except:
            currency = ""

        car = {
            "url": url,
            "source": source,
            "category": category,
            "brand": brand,
            "model": model,
            "generation": generation,
            "year": year,
            "mileage": mileage,
            "capacity": capacity,
            "fuel": fuel,
            "horse_power": horse_power,
            "transmission": transmission,
            "drive": drive,
            "type": type,
            "doors": doors,
            "seats": seats,
            "color": color,
            "origin": origin,
            "first_owner": first_owner,
            "not_crashed": not_crashed,
            "aso_service": aso_service,
            "used": used,
            "price": price,
            "currency": currency,
        }

        # car = {"url": url,"source": source}

        df = df.append(car, ignore_index=True)
        df.to_csv("results.csv", index=False)
    return df
