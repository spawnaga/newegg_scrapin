#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:28 2021

@author: alex
"""

from core import crawler, scraper, utils, purchase
from html import unescape
import re
from re import sub
from decimal import Decimal
import time

NEWEGG_URL = "https://newegg.com"
NEWEGG_RTX_PATH = "/p/pl?N=100007709%20601359511%20601357282%204814%208000&PageSize=96"
# NEWEGG_RTX_PATH = "/p/pl?d=gpus&N=8000%204814%20601357282%20100007709&PageSize=96"


def clean_price(price):
    price_contains_numbers = bool(re.search(r'[\d+,]+(\d+)', price))
    if price_contains_numbers:
        # split the price to remove the empty space and pick the first item
        price = unescape(price).split()[0]

    return price


def get_rtx_prices(tree):
    price_selector = "//li[contains(@class, 'price-current')]"
    price_text = scraper.get_text(tree, price_selector)
    return list(map(lambda price: clean_price(price), price_text))


def get_rtx_names(tree):
    name_selector = "//div[@class='item-info']/a"
    return scraper.get_text(tree, name_selector)


def get_rtx_links(tree):
    link_selector = "//div[@class='item-info']/a"
    return scraper.get_attributes(tree, link_selector, "href")


def get_rtx_stock_information(tree):
    item_selector = "//div[@class='item-container']"
    child_selector = "div[@class='item-info']/p[contains(., 'OUT OF STOCK')]"
    stock_details = scraper.get_children_text(
        tree, item_selector, child_selector)

    # set None to in stock, handles case when item has no "out of stock" label
    return list(map(lambda element: element or "IN STOCK", stock_details))


def get_rtx_ids(tree):
    item_id_selector = "//ul[@class='item-features']/li[contains(., 'Item #')]/text()"
    return scraper.get_nodes(tree, item_id_selector)


def get_rtx_items(tree):
    prices = get_rtx_prices(tree)
    names = get_rtx_names(tree)
    links = get_rtx_links(tree)
    ids = get_rtx_ids(tree)
    stock_details = get_rtx_stock_information(tree)
    items = []

    for index, price in enumerate(prices):
        name = names[index]
        link = links[index]
        stock = stock_details[index]
        id = ids[index]

        items.append({
            'name': name,
            'link': link,
            'stock': stock,
            'price': price,
            'id': id
        })

    return items

f = open(r"C:\Projects\newegg_scrapin\core\Webshare 1000 proxies.txt", "r")
ip = f.readline()

while True:
    try:
        proxies = {
         "http": ip[:-1],
         "https": ip[:-1],
        }
        crawl_url = f"{NEWEGG_URL}{NEWEGG_RTX_PATH}"
        try:
            html = crawler.crawl_html(crawl_url, proxies)
        except:
            ip = f.readline()
            continue
        tree = scraper.get_tree(html)
        rtx_items = get_rtx_items(tree)
        print(len(rtx_items))
        if len(rtx_items) == 0:
            ip = f.readline()
            print('proxy ip is blocked/malfunction switching/skipping to a different proxy')
            continue
        for i in range(len(rtx_items)):
            value = float(Decimal(sub(r'[^\d.]', '', rtx_items[i]['price']))) if rtx_items[i]['price'] != "" else 0
        
            if 100< value < 2400 and not 'open' in rtx_items[i]['name'] and not rtx_items[i]['stock'] == "OUT OF STOCK":
                
                print(f"{rtx_items[i]['name']}: {rtx_items[i]['stock']}")
                print("link : {rtx_items[i]['link']}")
                value = Decimal(sub(r'[^\d.]', '', rtx_items[i]['price']))
                print(value)
                purchase.work(rtx_items[i]['link'])
            
        time.sleep(2)
    except Exception as e:
        print(e)
        print('connection interrupted, trying again')
        
    except KeyboardInterrupt:
        break
        