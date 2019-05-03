import uuid
import os
import datetime

from common.mongo_database import MongoDatabase

COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION")


class StockPrice:

    def __init__(self, stock_code, price):
        self.stock_code = stock_code
        self.price = price
        self.insert_time = datetime.datetime.utcnow()
        self.exchange = "NSE"

    def save_to_mongo(self):
        MongoDatabase.insert(COLLECTION_NAME, self.to_json())

    def to_json(self):
        return {
            "stock_code": self.stock_code,
            "price": self.price,
            "insert_time": self.insert_time,
            "exchange": self.exchange
        }

