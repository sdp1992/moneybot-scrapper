import os
import time

from src.scrapper import Scrapper
from model.stock import StockPrice
from common import strings, load_links


def main():
    strings.refresh()  # Loading strings
    load_links.refresh()  # Loading stock-link dictionary

    stocks = list(load_links.get_list_of_stocks()) # Getting list of stocks to track

    while True:
        for stock in stocks:
            price = Scrapper.scrap(load_links.get_link(stock))
            stock_price = StockPrice(stock, price)
            stock_price.save_to_mongo()
            # print(StockPrice(stock, price).json())
            time.sleep(10)




