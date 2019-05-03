import pymongo
import os
from typing import Dict


class MongoDatabase:
    URI = os.environ.get("MONGODB_URI")
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        MongoDatabase.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return MongoDatabase.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return MongoDatabase.DATABASE[collection].find_one(query)


