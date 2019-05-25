import os
import time

from src.scrapper import Scrapper
from model.stock import StockPrice
from common import load_links


def main():
    load_links.refresh()  # Loading stock-link dictionary

    stocks = load_links.get_list_of_stocks() # Getting list of stocks to track

    while True:
        for stock in stocks:
            price = Scrapper.scrap(load_links.get_link(stock))
            stock_price = StockPrice(stock, price)
            stock_price.save_to_mongo()
            time.sleep(10)




