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
import pandas as pd

url = "https://hashbox.monster/goods/detail/1" 
res = requests.get(url) 
res.raise_for_status()
driver = webdriver.Chrome()
driver.get(url)
data = []

folder_name = "images"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

time.sleep(5)

elements = driver.find_elements(By.CSS_SELECTOR,"div.item_rank.goods_detail_trigger")
#print(type())
for i in range(12,13) :
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
    # 상품가격
    product_price = driver.find_element(By.CSS_SELECTOR, "div.price_data > div > div:nth-child(2)").text.strip()
    product_price = int(re.sub("[^0-9]","",product_price))
    # 메인 사진.. main_file 은 엑셀 저장용으로 만듬 알파벳을 B 로 했는데 뭘로 바꿀지 생각해야할듯..
    main_file = "B_" + product_name +".jpg"
    main_filename = os.path.join(folder_name, "B_" + product_name + ".jpg")
    # 상세정보 사진
    detail_filename = os.path.join(folder_name, product_name + ".webp")
    urllib.request.urlretrieve(mainsrc, filename=main_filename)
    print(f"{i}번째 상품 등록 완료!")
    # 모달창 닫기
    driver.find_element(By.CSS_SELECTOR,"div.goods_detail_modal > div.goods_detail_modal_close").click()

    data.append([product_name, main_file, product_price, detailsrc, "", "3000", "N"])

print(data)

df = pd.DataFrame(data, columns=["상품명", "이미지명", "가격", "상세정보", "원가", "배송비", "묶음여부"])

df.to_excel("test.xlsx", index=False)

time.sleep(3)
