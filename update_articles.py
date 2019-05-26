import os
import time
import json
from dotenv import load_dotenv
load_dotenv('.env')

from pymongo.errors import ConnectionFailure

from model.news import News


def run_updater():
    stock_dict = json.load(open('resources/stock_links.json'))
    stock_list = list(json.load(open('resources/stock_links.json')))
    for stock in stock_dict.keys():
        try:
            news = News.get_by_stock_code(collection="news_articles", stock_code=stock)
            if news is None:
                new_news = News(stock_code=stock)
                new_news.load_articles(query=stock_dict[stock]['name'])
                new_news.update_articles()
            else:
                news.load_articles(stock_dict[stock]['name'])
                news.update_articles()
            print("Updated: " + stock)
        except ConnectionFailure:
            print("Unable to connect Mongodb...")
        finally:
            time.sleep(10)

    print("Update completed...")


if __name__ == '__main__':
    run_updater()
