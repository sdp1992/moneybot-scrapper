import uuid
import os
from datetime import datetime
import json
from dataclasses import dataclass, field

from common.mongo_database import MongoDatabase
from model.model import Model

COLLECTION_NAME = os.environ.get("MONGODB_COLLECTION")

STOCK_LIST = list(json.load(open("resources/stock_links.json")).keys())


@dataclass(eq=False)
class StockPrice(Model):
    stock_code: str
    price: float
    collection: str = field(default="stock_prices")
    insert_time: datetime = field(default_factory=lambda: datetime.utcnow())
    exchange: str = field(default="NSE")
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def save_to_mongo(self):
        MongoDatabase.insert(self.collection, self.json())

    def json(self):
        return {
            "_id": self._id,
            "stock_code": self.stock_code,
            "price": self.price,
            "insert_time": self.insert_time,
            "exchange": self.exchange
        }

