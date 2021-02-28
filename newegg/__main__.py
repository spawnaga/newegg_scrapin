#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:28 2021

@author: alex
"""

from core import crawler, scraping

NEWEGG_URL = "https://newegg.com"
NEWEGG_RTX_PATH = "/p/pl?N=100007709%20601357282&PageSize=96"

def get_rtx_prices(tree):
    price_selector = "//li[contains(@class, 'price-current')]"
    return scraping.get_text(tree, price_selector)


crawl_url = f"{NEWEGG_URL}{NEWEGG_RTX_PATH}"
html = crawler.crawl_html(crawl_url)
tree = scraping.get_tree(html)
prices = get_rtx_prices(tree)
print(prices)