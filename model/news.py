import os
import requests
import uuid
from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict

from model.model import Model


@dataclass(eq=False)
class News(Model):
    stock_code: str
    collection: str = field(default="news_articles")
    articles: list = field(default_factory=list)
    last_updated: datetime = None
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_articles(self):
        url = "https://newsapi.org/v2/everything?q=" + self.stock_code + "&apiKey=" + os.environ.get("GOOGLE_NEWS_API_KEY")
        response = requests.get(url=url).json()
        articles = response['articles']
        self.articles = articles
        self.last_updated = datetime.utcnow()

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "stock_code": self.stock_code,
            "collection": self.collection,
            "articles": self.articles,
            "last_updated": self.last_updated
        }
