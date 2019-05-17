import os
import time
import json
from dotenv import load_dotenv
load_dotenv('.env')

from pymongo.errors import ConnectionFailure

from model.news import News


def run_updater():
    stock_list = list(json.load(open('resources/stock_links.json')))
    for stock in stock_list:
        try:
            news = News.get_by_stock_code(collection="news_articles", stock_code=stock)
        except ConnectionFailure:
            print("Unable to connect Mongodb...")
        else:
            if news is None:
                new_news = News(stock_code=stock)
                new_news.load_articles()
                new_news.update_articles()
            else:
                news.load_articles()
                news.update_articles()
            print("update: " + stock)
        finally:
            time.sleep(10)

    print("Update completed.")


if __name__ == '__main__':
    run_updater()
