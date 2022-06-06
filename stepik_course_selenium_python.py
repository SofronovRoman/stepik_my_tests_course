# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:21:03 2022

@author: User
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Service = Service(r'D:\programs\Python\chromedriver_win32\chromedriver.exe')




link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome(service=Service)
    # browser.implicitly_wait(5)
    browser.get(link)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.TAG_NAME, "button").click()     
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)                              
    browser.find_element(By.ID, "solve").click()



    
    
    # browser.find_element(By.TAG_NAME, "button").click()
    # browser.switch_to.window(browser.window_handles[1])
    # confirm = browser.switch_to.alert
    # confirm.accept()
    # x = browser.find_element(By.ID, "input_value").text
    # y = calc(x)
    # browser.find_element(By.ID, "answer").send_keys(y)    
    # browser.execute_script("window.scrollBy(0, 150);")
    # browser.find_element(By.ID, "robotCheckbox").click()
    # browser.find_element(By.ID, "robotsRule").click()
    # browser.find_element(By.TAG_NAME, "button").click()
    
    
finally:
    time.sleep(5)
    browser.quit()