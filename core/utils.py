#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:30:28 2021

@author: alex
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def get_login_code():
    options = Options() 
    # options.add_argument("--headless")
    options.add_argument("start-maximized")
    chrome_driver_exe_path = r"C:\chromedriver.exe"
    web = webdriver.Chrome(executable_path=chrome_driver_exe_path, options=options)
    web.get("https://www.hotmail.com")
    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'/html/body/header/div/aside/div/nav/ul/li[2]/a'))).click()

    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="i0116"]'))).send_keys('ali.ghalibe@hotmail.com')
    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="idSIButton9"]'))).click()

    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="i0118"]'))).send_keys('p!@h7kc7zYex4bt')
    time.sleep(0.5)
    web.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(0.5)
    WebDriverWait(web,1).until(EC.presence_of_element_located((By.CLASS_NAME,'_3zJzxRam-s-FYVZNqcZ0BW'))).click()
    time.sleep(0.5)
    content = web.find_element_by_xpath('//*[@id="ReadingPaneContainerId"]/div/div/div/div[2]/div[1]/div/div[3]/div/div/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table/tbody/tr[4]/td').text
    web.close()
    return content


