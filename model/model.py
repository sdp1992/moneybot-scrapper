
from typing import List, Dict, Union, Type, TypeVar
from abc import ABCMeta, abstractmethod


from common.mongo_database import MongoDatabase

T = TypeVar('T', bound='Model')


class Model(metaclass=ABCMeta):
    stock_code: str
    collection: str
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], collection: str, attribute: str, value: Union[str, Dict]) -> Union[T, None]:
        try:
            return cls(**MongoDatabase.find_one(collection, {attribute: value}))
        except TypeError:
            return None

    @classmethod
    def find_many_by(cls: Type[T], collection: str, attribute: str, value: Union[str, Dict], top_n: int) -> List[T]:
        return [cls(**elem) for elem in MongoDatabase.find(collection, {attribute: value}).limit(top_n)]

    @classmethod
    def get_by_stock_code(cls: Type[T], collection: str, stock_code: str) -> Union[T, None]:
        return cls.find_one_by(collection, "stock_code", stock_code)
