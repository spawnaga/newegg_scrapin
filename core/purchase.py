# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:44:27 2021

@author: Ghailb
"""

from core import utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

DEFAULT_MAX_TIMEOUT = 20

def get_timeout(timeout=DEFAULT_MAX_TIMEOUT):
    return time.time() + timeout
url = 'https://www.newegg.com/p/2MB-001H-00006?Description=thermal%20paste&cm_re=thermal_paste-_-9SIABW9BFE5088-_-Product&quicklink=true'
def work(url):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    timeout = get_timeout()
    options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
    chrome_driver_exe_path = r"C:\chromedriver.exe"
    web = webdriver.Chrome(executable_path=chrome_driver_exe_path, options=options)
    tries = 10
    tried = 0
    options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
    while True:
        try:
            tried +=1
            web.get(url)            
            web.maximize_window()
            time.sleep(0.3)
            if time.time() > timeout or tried == tries:
                print('time_out')
                return
            try:
                web.find_element_by_xpath('//*[@id="popup-close"]').click()
            except:
                pass
            try:
                stock = web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/div/span').text
            except:
                stock = ''
            if stock == 'OUT OF STOCK':
                break
            web.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[4]/div[1]/div[1]/a/div[2]').click()
            web.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').send_keys("ali.ghalibe@hotmail.com")
            web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
            time.sleep(0.5)
            
            try:
                web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[2]/div')
                code = utils.get_login_code()
                web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[1]').send_keys(code)
                web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
                break
            except:
                web.find_element_by_xpath('//*[@id="labeled-input-password"]').send_keys('Cinquant15')
                web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
                break
        except Exception as error:
            print(error)
    timeout = get_timeout()
    tried = 0
    while not stock == 'OUT OF STOCK':
        if time.time() > timeout or tried == tries:
                print('time_out')
                return
        tried +=1
        try:
            if time.time() > timeout:
                break
            time.sleep(0.3)
            web.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button').click()
            time.sleep(0.3)
            web.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]').click()
            time.sleep(0.3)
            try:
                web.find_element_by_xpath('//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]').click()
                time.sleep(0.3)
                web.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button').click()
                time.sleep(0.3)
            except:
                web.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button').click()
                time.sleep(0.3)

            time.sleep(1.0)
            web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button').click()
            time.sleep(1.0)
            web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button').click()
            time.sleep(2.5)
            try:
                web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[1]/div/label/div[4]/input').send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,'743')
                time.sleep(2.5)
            except :
                try:
                    web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[1]/div/label/div[4]/input').send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,'743')
                except:
                    time.sleep(2.5)
                    web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[1]/div/label/div[4]/input').send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,'743')
            time.sleep(1.0)
            web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[3]/button').click()
            time.sleep(1.0)
            web.find_element_by_xpath('//*[@id="btnCreditCard"]').click()
            break
        except Exception as e:
            print(e)
            web.get(url)
    if stock == 'OUT OF STOCK':
        print('Item sold out, better luck next time')
    
    
work(url)