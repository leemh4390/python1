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

elements  = soup.select("div.product_element")
data = []
discount = 0

for element in elements :

    name = element.find("div","product_name").text.strip()
    price = int(re.sub(r'[^0-9]', '', element.find("div","product_price").text.strip()))
    probability = element.find("div", "product_probability").text.strip()

    if price > 50000000 :
        grade = 'Ground X'
    elif price >  5000000 :
        grade = 'Ground A'
    elif price > 500000 :
        grade = 'Ground B'
    elif price >= 135000 :
        grade = 'Ground C'
    elif price >= 110000 :
        grade = 'Ground D'
    else :
        grade = 'Ground E'

    data.append([grade, name, price, '',probability]) 
    
print(data)

df = pd.DataFrame(data, columns=["등급", "상품명", "가격", "할인율", "당첨확률"])

df.to_excel("hash2.xlsx", index=False)




