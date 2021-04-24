from links import get_pages_links, get_offer_links
from scrap_data import scrap


def main():
    pages = get_pages_links()
    offers = get_offer_links(pages, only_100=True)
    scrap(offers)


if __name__ == "__main__":
    main()
