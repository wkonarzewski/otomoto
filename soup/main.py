from links import get_pages_links, get_offer_links
from scrap_data import scrap


def main():
    pages = get_pages_links()
    offers = get_offer_links(pages, only_100=True)
    scrap(offers).to_csv("bs_cars.csv", index=False) # exporting dataframe to csv file


if __name__ == "__main__":
    main()
