from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests 
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import os
import re

url = "https://hashbox.monster/goods/detail/1" 
res = requests.get(url) 
res.raise_for_status()
driver = webdriver.Chrome()
driver.get(url)

folder_name = "images"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

time.sleep(5)

#elements = str(driver.find_elements(By.CSS_SELECTOR,"div.item_rank.goods_detail_trigger"))
#for i in range(1,elements) :
for i in range(1,2) :
    action = ActionChains(driver)
    print(f"{i}번째 시작..!")
    product_list = driver.find_element(By.CSS_SELECTOR, f"div.product_guide > div:nth-child({i})")
    action.move_to_element(product_list).perform()
    # n번째 상품으로 이동 후 클릭 클릭
    driver.find_element(By.CSS_SELECTOR, f"div.product_guide > div:nth-child({i}) > div:nth-child(1)").click()
    time.sleep(3)
    mainsrc = driver.find_element(By.CSS_SELECTOR, "div.goods_detail > div.goods_main_image > img").get_attribute('src')
    detailsrc = driver.find_element(By.CSS_SELECTOR, "div.goods_detail > div.goods_detail_image > img").get_attribute('src')
    # 상품명
    product_name = driver.find_element(By.CSS_SELECTOR, "div.goods_title.goods_detail_modal_goods_title.suit_medium_font").text.strip()
    product_price = driver.find_element(By.CSS_SELECTOR, "div.price_data > div > div:nth-child(2)").text.strip()
    product_price = int(re.sub("[^0-9]","",product_price))
    print(product_price)
    main_filename = os.path.join(folder_name, product_name + ".jpg")
    detail_filename = os.path.join(folder_name, product_name + ".webp")
    urllib.request.urlretrieve(mainsrc, filename=main_filename)
    # urllib.request.urlretrieve(detailsrc, filename=detail_filename)
    print(f"{i}번째 상품 등록 완료!")
    driver.find_element(By.CSS_SELECTOR,"div.goods_detail_modal > div.goods_detail_modal_close").click()
 


time.sleep(3)

