from selenium import webdriver
from os.path import abspath
from os import path
from time import sleep
import pickle
from core import utils

options = webdriver.ChromeOptions()
options.add_argument(r"C:\Users\Ghailb\AppData\Local\Google\Chrome\User Data\Default")  # Path to your chrome profile or you can open chrome and type: "chrome://version/" on URL

chrome_driver_exe_path = abspath("C:\chromedriver.exe")  # download from https://chromedriver.chromium.org/downloads
assert path.exists(chrome_driver_exe_path), 'chromedriver.exe not found!'
web = webdriver.Chrome(executable_path=chrome_driver_exe_path, options=options)

web.get("https://www.newegg.com")
web.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[4]/div[1]/div[1]/a/div[2]').click()
web.find_element_by_xpath('//*[@id="labeled-input-signEmail"]').send_keys("ali.ghalibe@hotmail.com")
web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
sleep(0.2)
try:
    code = utils.get_login_code()
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[3]/form/div/div[3]/div/input[1]').send_keys(code)
    web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
except:
    web.find_element_by_xpath('//*[@id="labeled-input-password"]').send_keys('Cinquant15')
    web.find_element_by_xpath('//*[@id="signInSubmit"]').click()
pickle.dump(web.get_cookies() , open(r"C:\Projects\newegg_scrapin\newegg\core\cookies.pkl","wb"))
web.close()