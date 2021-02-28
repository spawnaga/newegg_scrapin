#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:26 2021

@author: alex
"""

import requests


def crawl_html(url):
    response = requests.get(url)
    return response.content # returns the content in bytes (required later for lxml)
