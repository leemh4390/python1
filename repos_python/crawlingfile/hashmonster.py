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

# 총 요소 개수를 저장할 변수 초기화
total =  160
number = "00000" 

# 폴더명
folder_name = "images"

# 폴더명이 없으면 생성함
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

time.sleep(1)

# 카테고리 선택..
categories = driver.find_elements(By.CSS_SELECTOR, "div.complicated_list > div")
# 전자, 명품(남), 명품(여) 만 선택하기 위해서 추가함
category_index = [0]
#selector = ["item_rank.goods_detail_trigger", "small_box.ground_b.goods_detail_trigger", "small_box.ground_normal.goods_detail_trigger"]
selector = ["small_box.ground_normal.goods_detail_trigger"]

for cate in category_index :
    action = ActionChains(driver)
    action.move_to_element(categories[cate]).perform()
    categories[cate].click()
    time.sleep(1)
    # selector 의 값을  value 에 대입함
    for value in range(len(selector)) :
        elements = driver.find_elements(By.CSS_SELECTOR,f"div.{selector[value]}")
        for i in range(140,160) :
            print(f"{i}번째 시작..!")
            type = "n_"
            product_list = driver.find_element(By.CSS_SELECTOR, f"div.{selector[value]}:nth-child({i})")
            action.move_to_element(product_list).perform()
            # n번째 상품으로 이동 후 클릭
            driver.find_element(By.CSS_SELECTOR, f"div.{selector[value]}:nth-child({i}) > div:nth-child(1)").click()
            time.sleep(2)
            # main src
            mainsrc = driver.find_element(By.CSS_SELECTOR, "div.goods_detail > div.goods_main_image > img").get_attribute('src')
            # detail src
            detailsrc = driver.find_element(By.CSS_SELECTOR, "div.goods_detail > div.goods_detail_image > img").get_attribute('src')
            # 상품명
            product_name = driver.find_element(By.CSS_SELECTOR, "div.goods_title.goods_detail_modal_goods_title.suit_medium_font").text.strip()
            # 상품가격
            product_price = driver.find_element(By.CSS_SELECTOR, "div.price_data > div > div:nth-child(2)").text.strip()
            product_price = int(re.sub("[^0-9]","",product_price))
            # 5자리로 0으로 채워진 숫자로 설정
            total += 1
            main_img_name = f"{type}{number}{total}.jpg"  
            main_filename = os.path.join(folder_name, main_img_name)
            detail_filename = os.path.join(folder_name, product_name + ".webp")
            try :
                urllib.request.urlretrieve(mainsrc, filename=main_filename)
            except :  
                # 상품명에 특수문자가 있으면 발생하는 에러
                # 상품명의 특수문자를 제거하고 저장함
                product_name = re.sub(r'[\\|\/|:|\*|\?|!|"|<|>₩]', '', product_name)
                urllib.request.urlretrieve(mainsrc, filename=main_filename)
            print(f"{i}번째 상품 등록 완료!")                        
            # 모달창 닫기
            driver.find_element(By.CSS_SELECTOR,"div.goods_detail_modal > div.goods_detail_modal_close").click()
            time.sleep(2)
            data.append([product_name, main_img_name, product_price, detailsrc, "", "3000", "N"])
            print(main_img_name)
df = pd.DataFrame(data, columns=["상품명", "이미지명", "가격", "상세정보", "원가", "배송비", "묶음여부"])

df.to_excel("test.xlsx", index=False)
time.sleep(2)
