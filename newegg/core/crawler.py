#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:26 2021

@author: alex
"""

import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions() 
# options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
# w = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe", chrome_options=options)

def crawl_html(url):
    response = requests.get(url)
    print('**************************************')
    return response.content # returns the content in bytes (required later for lxml)
