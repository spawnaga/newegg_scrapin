# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:37:00 2021

@author: Ghailb
"""
from selenium import webdriver
import pickle
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver.exe')
cookies = pickle.load(open(r"C:\Projects\newegg_scrapin\newegg\core\cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)
driver.get('https://www.newegg.com/')
