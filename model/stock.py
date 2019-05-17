import uuid
import os
from datetime import datetime
import json
from dataclasses import dataclass, field
from pymongo.errors import ConnectionFailure

from common.mongo_database import MongoDatabase
from model.model import Model

COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION")

STOCK_LIST = list(json.load(open("resources/stock_links.json")).keys())


@dataclass(eq=False)
class StockPrice(Model):
    stock_code: str
    price: float
    insert_time: datetime = field(default_factory=lambda: datetime.utcnow())
    exchange: str = field(default="NSE")
    _id: str = field(default=None)

    def save_to_mongo(self, collection="stock_prices"):
        try:
            MongoDatabase.insert(collection, self.json())
        except ConnectionFailure:
            print("Unable to connect MongoDB...")

    def json(self):
        return {
            "stock_code": self.stock_code,
            "price": self.price,
            "insert_time": self.insert_time,
            "exchange": self.exchange
        }

