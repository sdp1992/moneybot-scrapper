import pymongo
import os
from typing import Dict, Union


class MongoDatabase:
    URI = os.environ.get("MONGODB_URI")
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    @staticmethod
    def update(collection: str, query, data) -> None:
        MongoDatabase.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def insert(collection: str, data) -> None:
        MongoDatabase.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return MongoDatabase.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Union[Dict, None]:
        return MongoDatabase.DATABASE[collection].find_one(query)


