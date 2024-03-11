from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re

url = "https://hashbox.monster/probability" 
res = requests.get(url) 
res.raise_for_status()
soup = BeautifulSoup(res.content, "html.parser")
driver = webdriver.Chrome()

def selenium_test():
    data = []
    driver.get(url)

    time.sleep(3)

    driver.find_element(By.CLASS_NAME, 'hashbox.bronze').click()

    time.sleep(5)
    
    
    # 해당 data-id 값을 가진 요소를 찾음
    for i in range(1,6) :
        selector = f"complicated:nth-child({i})"
        data_element = driver.find_element(By.CLASS_NAME, selector).click()
    
        elements = driver.find_elements(By.CLASS_NAME, "product_element")

        for element in elements :
            # name = element.find_element(By.CLASS_NAME, "product_name").text
            # price = int(re.sub(r'[^0-9]', '',element.find_element(By.CLASS_NAME, "product_price").text))
            # probability = element.find_element(By.CLASS_NAME, "product_probability").text

            # if price    >= 5000000 :
            #     grade = 'Ground X'
            # elif price  >= 500000 :
            #     grade = 'Ground A'
            # elif price  >= 90000 :
            #     grade = 'Ground B'
            # elif price  >= 18000 :
            #     grade = 'Ground C'
            # elif price  >= 13000 :
            #     grade = 'Ground D'
            # else :
            #     grade = 'Ground E'        

            # data.append([grade, name, price, '',probability])
            print(element)
    time.sleep(10)

selenium_test()