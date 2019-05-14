import os
import time

from common import load_links
from src.scrapper import Scrapper
from model.stock import StockPrice


def main():

    stocks = list(load_links.get_list_of_stocks())

    while True:
        for stock in stocks:
            price = Scrapper.scrap(load_links.get_link(stock))
            stock_price = StockPrice(stock, price)
            stock_price.save_to_mongo()
            print(StockPrice(stock, price).json())
            time.sleep(20)




