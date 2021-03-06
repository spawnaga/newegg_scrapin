# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 18:44:27 2021

@author: Ghailb
"""

from core import utils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

start_time = time.time()
def get_timeout(timeout=120):
    return time.time() + timeout
# url = 'https://www.newegg.com/amd-ryzen-7-3700x/p/N82E16819113567?Item=N82E16819113567&quicklink=true'
def work(url):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    timeout = get_timeout()
    # options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
    chrome_driver_exe_path = r"C:\chromedriver.exe"
    web = webdriver.Chrome(executable_path=chrome_driver_exe_path, options=options)
    tries = 1
    tried = 0
    cookies = pickle.load(open(r"C:\Projects\newegg_scrapin\newegg\core\cookies.pkl", "rb"))
    web.get('https://www.newegg.com/')
    for cookie in cookies:
        web.add_cookie(cookie)
    
    # options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default") #Path to your chrome profile
    web.get(url)
    try:
        web.find_element_by_xpath('//*[@id="popup-close"]').click()
    except:
        pass
    try:
        stock = web.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/div/span').text
    except Exception:
        stock = ''
    if stock == 'OUT OF STOCK':
        print('Out of stock, better luck next time')
        return
    else:
        tries = 0
        while True:
            try:
                tries +=1
                WebDriverWait(web,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ProductBuy"]/div/div[2]/button'))).click()
                break
            except:
                if tries > 3:
                    web.refresh()
                    continue
                return


    try:
        WebDriverWait(web,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]'))).click()
    except:
        pass
    timeout = get_timeout()
    tried = 0
    while not stock == 'OUT OF STOCK':
        try:
            if time.time() > timeout or tried == tries:
                    print('time_out')
                    return
            tried +=1
            if time.time() > timeout:
                break
            # try:
            #     web.find_element_by_xpath('//*[@id="modal-pc-builder-check"]/div/div/div/div/div/div/div[2]').click()
            # except:
            #     pass
            try:
                WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]'))).click()
            except:
                pass
            try:
                WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]'))).click()
            except:
                pass
            try:
                WebDriverWait(web,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button'))).click()
            except:
                try:
                    WebDriverWait(web,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]'))).click()
                except:
                    pass
                try:
                    WebDriverWait(web,3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button'))).click()
                except:
                    pass
                try:
                    WebDriverWait(web,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="labeled-input-password"]'))).send_keys('Cinquant15')
                    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="signInSubmit"]'))).click()
                except:
                    code = utils.get_login_code()
                    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[1]'))).send_keys(code)
                    web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
                try:
                    WebDriverWait(web,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]'))).click()
                    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]'))).click()
                except:
                    # try:
                    #     WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]'))).click()
                    # except:
                    pass
                try:
                    WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]'))).click()
                    # WebDriverWait(web,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button'))).click()
                except:
                    pass
                time.sleep(0.5)
                
            # try:
            #     WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="labeled-input-signEmail"]'))).send_keys('ali.ghalibe@hotmail.com')
            #     web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
            # except: 
            #     pass
            try:
                WebDriverWait(web,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="labeled-input-password"]'))).send_keys('Cinquant15')
                web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
            except:
                pass
            WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button'))).click()
            time.sleep(0.8)
            element = web.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button')
            web.execute_script("arguments[0].click();", element)
            time.sleep(0.8)
            WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[3]/div[1]/div/label/div[4]/input'))).send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,'743')
            WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[3]/button'))).click()
            time.sleep(1)
            WebDriverWait(web,1).until(EC.presence_of_element_located((By.XPATH,'//*[@id="btnCreditCard"]'))).click()
            print('all went well')
            break
        except:
            return
        if stock == 'OUT OF STOCK':
            print('Item sold out, better luck next time')

    
    
# work(url)
print("--- %s seconds ---" % (time.time() - start_time))