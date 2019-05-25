import os
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict
from newsapi import NewsApiClient
from pymongo.errors import ConnectionFailure
from newsapi.newsapi_exception import NewsAPIException

from model.model import Model
from model.errors import InvalidNewsApiError
from common.mongo_database import MongoDatabase


api = NewsApiClient(api_key=os.environ.get("GOOGLE_NEWS_API_KEY"))


@dataclass(eq=False)
class News(Model):
    stock_code: str
    articles: list = field(default_factory=list)
    last_updated: datetime = None
    _id: str = field(default=None)

    def load_articles(self):
        try:
            response = api.get_everything(q=self.stock_code + " stock news",
                                          language='en', sort_by='popularity', page_size=10)

            if response['status'] is not "ok":
                raise InvalidNewsApiError("Invalid response.")

        except NewsAPIException:
            print("Unable to get latest news...")
        except InvalidNewsApiError as e:
            print(e.message)

        else:
            self.articles = response['articles']
            self.last_updated = datetime.utcnow()

    def update_articles(self, collection="news_articles"):
        try:
            MongoDatabase.update(collection, {"stock_code": self.stock_code}, self.json())
        except ConnectionFailure:
            print("Unable to connect to Mongodb...")

    def json(self) -> Dict:
        return {
            "stock_code": self.stock_code,
            "articles": self.articles,
            "last_updated": self.last_updated
        }
