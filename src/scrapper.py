import os
from bs4 import BeautifulSoup
import requests
import requests.exceptions as RequestErrors

from model.errors import *


class Scrapper:

    def __init__(self, stock_code, price):
        pass

    @staticmethod
    def scrap(link):
        try:
            response = requests.get(link)
            if response.status_code != 200:
                return 0
            try:
                content = response.content
                soup = BeautifulSoup(content, "html.parser")
                element = soup.find("span", {"id": "Nse_Prc_tick"}).strong.get_text()
                string_price = element.strip()
                price = float(string_price)
                return price
            except UnableToExtractError as e:
                print("Unable to extract information.")
            finally:
                response.close()

        except RequestErrors as e:
            print("Unable to get response")





