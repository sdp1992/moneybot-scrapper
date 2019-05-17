
"""
common.load_links
By default, uses `resources/stock_links.json` file inside the `resources` top-level folder.
Run `common.load_links.refresh()`.
"""

import json

cached_links = {}


def refresh():
    print("Loading links for stock codes...")
    global cached_links
    with open("resources/stock_links.json") as f:
        cached_links = json.load(f)


def get_link(code):
    return cached_links[code]


def get_list_of_stocks():
    return cached_links.keys()

