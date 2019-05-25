
"""
common.load_links
By default, uses `resources/stock_links.json` file inside the `resources` top-level folder.
Run `common.load_links.refresh()`.
"""

import json

cached_stocks = {}


def refresh():
    print("Loading links for stocks...")
    global cached_stocks
    with open("resources/stock_links.json") as f:
        cached_stocks = json.load(f)


def get_link(stock_code):
    return cached_stocks[stock_code]['link']


def get_list_of_stocks():
    return list(cached_stocks.keys())

