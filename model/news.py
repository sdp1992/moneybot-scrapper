import os
import uuid
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
    last_updated: datetime = field(default_factory=datetime.utcnow)
    _id: str = field(default=uuid.uuid4().hex)

    def load_articles(self, query):
        try:
            response = api.get_everything(q=query + " stock news",
                                          language='en', sort_by='relevancy', page_size=10)

            # if response['status'] is not "ok":
            #     raise InvalidNewsApiError("Invalid response.")

            self.articles = response['articles']
            self.last_updated = datetime.utcnow()

        except NewsAPIException:
            print("Unable to get latest news...")
        except InvalidNewsApiError as e:
            print(e.message)

    def update_articles(self, collection="news_articles"):
        try:
            self.update_to_mongo(collection, {"stock_code": self.stock_code}, self.json())
        except ConnectionFailure:
            print("Unable to connect to Mongodb...")

    def json(self) -> Dict:
        return {
            "stock_code": self.stock_code,
            "articles": self.articles,
            "last_updated": self.last_updated
        }
