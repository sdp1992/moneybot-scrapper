import uuid
import os
import json
from datetime import datetime
from dataclasses import dataclass, field
from pymongo.errors import ConnectionFailure

from model.model import Model

COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION")

STOCK_LIST = list(json.load(open("resources/stock_links.json")).keys())


@dataclass(eq=False)
class StockPrice(Model):
    stock_code: str
    price: float
    insert_time: datetime = field(default_factory=lambda: datetime.utcnow())
    exchange: str = field(default="NSE")

    def save_to_mongo(self, collection="stock_prices"):
        try:
            self.insert_to_mongo(collection, self.json())
        except ConnectionFailure:
            print("Unable to connect MongoDB...")

    def json(self):
        return {
            "stock_code": self.stock_code,
            "price": self.price,
            "insert_time": self.insert_time,
            "exchange": self.exchange,
        }

