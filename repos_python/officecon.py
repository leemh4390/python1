from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re

schStartPrice = 5000
schEndPrice = 6500
page = 1
maximum = 0

url = f"https://www.officecon.co.kr/product/sales/list?page=1&schWord=&brandSeqs=239&brandSeqs=50&brandSeqs=48&brandSeqs=49&brandSeqs=279&brandSeqs=259&brandSeqs=256&brandSeqs=245&brandSeqs=231&brandSeqs=225&brandSeqs=215&brandSeqs=214&brandSeqs=200&brandSeqs=179&brandSeqs=116&brandSeqs=81&brandSeqs=61&brandSeqs=58&brandSeqs=54&brandSeqs=53&brandSeqs=46&brandSeqs=44&brandSeqs=43&brandSeqs=82&brandSeqs=280&brandSeqs=293&brandSeqs=296&brandSeqs=300&brandSeqs=299&schStartPrice={schStartPrice}&schEndPrice={schEndPrice}&orderGubun=POPULAR#header"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element(By.CLASS_NAME, "pg_page.pg_end").click()

current_url = driver.current_url

maximum = int(current_url.split('page=')[-1].split('&')[0])

for i in range(1, maximum+1) :
    url = f"https://www.officecon.co.kr/product/sales/list?page={i}&schWord=&brandSeqs=239&brandSeqs=50&brandSeqs=48&brandSeqs=49&brandSeqs=279&brandSeqs=259&brandSeqs=256&brandSeqs=245&brandSeqs=231&brandSeqs=225&brandSeqs=215&brandSeqs=214&brandSeqs=200&brandSeqs=179&brandSeqs=116&brandSeqs=81&brandSeqs=61&brandSeqs=58&brandSeqs=54&brandSeqs=53&brandSeqs=46&brandSeqs=44&brandSeqs=43&brandSeqs=82&brandSeqs=280&brandSeqs=293&brandSeqs=296&brandSeqs=300&brandSeqs=299&schStartPrice={schStartPrice}&schEndPrice={schEndPrice}&orderGubun=POPULAR#header"
    driver.get(url)
    
    product_list = driver.find_elements(By.CSS_SELECTOR, "div#product_list > ul > li")

    for j in range(0, 1) :
        product_name = driver.find_element(By.CLASS_NAME, "info02").text
        # 원가
        product_price = driver.find_element(By.CLASS_NAME, "price").text
        # 할인 가격
        product_disPrice = driver.find_element(By.CLASS_NAME, "dis_price").text.split()[1]
        # 할인율
        product_percent = driver.find_element(By.CLASS_NAME, "percent").text
        # 이미지
        product_image = driver.find_element(By.CSS_SELECTOR, "div#product_list img").get_attribute('src')
        # 상품 주소
        product_id = re.search(r'\d+', driver.find_element(By.CSS_SELECTOR, "div#product_list a").get_attribute('href')).group()
        product_url = "https://www.officecon.co.kr/product/sales/view?productId="+product_id

        print(product_url)



time.sleep(3)
