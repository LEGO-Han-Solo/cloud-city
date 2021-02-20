import re
from time import sleep

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from cloud_city.utils import get_str_timestamp
from cloud_city.constants import NAME_FIELD_NAME, PRICE_FIELD_NAME, PEREX_FIELD_NAME, IN_STOCK_FIELD_NAME, \
    TIMESTAMP_FIELD_NAME

URL_TEMPLATE = "https://www.legenio.cz/star-wars/?p={}"
DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/61.0.3163.100 Safari/537.36'}


class LegenioCzScrapper:
    def __init__(self, url_template=URL_TEMPLATE, headers=DEFAULT_HEADERS, timeout=2):
        self.url = url_template
        self.headers = headers
        self.timeout = timeout

    def scrap_legos(self, limit=float('inf')):
        scrapped_legos = []
        page_numbers = self._get_page_numbers()
        for page_num in tqdm(page_numbers):
            sleep(self.timeout)
            page = self._read_page(page_num)
            products = self._get_product_list(page)
            for product in products:
                scrapped_legos.append(self._parse_product(product))
                limit -= 1
                if limit < 1:
                    break
            if limit < 1:
                break
        return scrapped_legos

    def _parse_product(self, product):
        price = self._get_price(product)
        name = self._get_name(product)
        in_stock = self._in_stock(product)
        perex = self._get_perex(product)
        timestamp = get_str_timestamp()
        return {NAME_FIELD_NAME: name,
                PRICE_FIELD_NAME: price,
                IN_STOCK_FIELD_NAME: in_stock,
                PEREX_FIELD_NAME: perex,
                TIMESTAMP_FIELD_NAME: timestamp}

    def _read_page(self, page_num):
        response = requests.get(self.url.format(page_num), headers=self.headers)
        content = response.content
        parser = BeautifulSoup(content, "html.parser")
        return parser

    def _get_page_numbers(self):
        parser = self._read_page(1)
        pagenum_elements = parser.find("p", {"class": "listing"}).find_all("a")
        count_pages = max((int(el.get_text()) for el in pagenum_elements if el.get_text()))
        return [pagenum + 1 for pagenum in range(count_pages)]

    @staticmethod
    def _get_product_list(parser):
        products = parser.find("div", {"id": "products-list"}).find_all("div", {"class": "product"})
        products += parser.find("div", {"id": "products-list"}).find_all("div", {"class": "product news"})
        return products

    @staticmethod
    def _get_price(product):
        price = product.find("strong", {"class": "price"}).get_text().strip()
        price = re.sub(',', '.', price)
        price = re.sub(' ', '', price)
        price = re.match(r"\d+\.?\d+", price).group(0)
        return float(price)

    @staticmethod
    def _in_stock(product):
        if product.find("a", {"class": "fast-buy"}):
            return True
        return False

    @staticmethod
    def _get_name(product):
        return product.find("h2", {"class": "product-name"}).get_text().strip()

    @staticmethod
    def _get_perex(product):
        return product.find("div", {"class": "perex"}).get_text().strip()
