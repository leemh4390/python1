from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import urllib.request
import time
import requests 
import pandas as pd
import re
import os

schStartPrice = 5000
schEndPrice = 6500
page = 1
maximum = 0
total = 1
data = []
now = datetime.now()

# 폴더명
folder_name = "오피스콘 " + now.strftime('%Y%m%d')

# 폴더명이 없으면 생성함
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

url = f"https://www.officecon.co.kr/product/sales/list?page=1&schWord=&brandSeqs=239&brandSeqs=50&brandSeqs=48&brandSeqs=49&brandSeqs=279&brandSeqs=259&brandSeqs=256&brandSeqs=245&brandSeqs=231&brandSeqs=225&brandSeqs=215&brandSeqs=214&brandSeqs=200&brandSeqs=179&brandSeqs=116&brandSeqs=81&brandSeqs=61&brandSeqs=58&brandSeqs=54&brandSeqs=53&brandSeqs=46&brandSeqs=44&brandSeqs=43&brandSeqs=82&brandSeqs=280&brandSeqs=293&brandSeqs=296&brandSeqs=300&brandSeqs=299&schStartPrice={schStartPrice}&schEndPrice={schEndPrice}&orderGubun=POPULAR#header"
#url = "https://www.officecon.co.kr/product/sales/list?page=1&schWord=&brandSeqs=51&brandSeqs=35&brandSeqs=267&brandSeqs=62&brandSeqs=164&brandSeqs=36&brandSeqs=38&brandSeqs=63&brandSeqs=93&brandSeqs=168&brandSeqs=37&brandSeqs=255&brandSeqs=254&brandSeqs=251&brandSeqs=242&brandSeqs=241&brandSeqs=178&brandSeqs=71&brandSeqs=69&brandSeqs=60&brandSeqs=39&brandSeqs=34&brandSeqs=32&brandSeqs=281&brandSeqs=282&brandSeqs=294&schPrice2=Y&schStartPrice=&schEndPrice=&orderGubun=POPULAR#header"
driver = webdriver.Chrome()
driver.get(url)

try :
    endpage = driver.find_element(By.CLASS_NAME, "pg_page.pg_end").click()
    current_url = driver.current_url
    maximum = int(current_url.split('page=')[-1].split('&')[0])    
except :
    endpage = driver.find_elements(By.CSS_SELECTOR, "span.pg > a")
    maximum = int(re.sub(r'[^0-9]', '', endpage[len(endpage) - 1].get_attribute('onclick')))

for i in range(1, maximum+1) :
    url = f"https://www.officecon.co.kr/product/sales/list?page={i}&schWord=&brandSeqs=239&brandSeqs=50&brandSeqs=48&brandSeqs=49&brandSeqs=279&brandSeqs=259&brandSeqs=256&brandSeqs=245&brandSeqs=231&brandSeqs=225&brandSeqs=215&brandSeqs=214&brandSeqs=200&brandSeqs=179&brandSeqs=116&brandSeqs=81&brandSeqs=61&brandSeqs=58&brandSeqs=54&brandSeqs=53&brandSeqs=46&brandSeqs=44&brandSeqs=43&brandSeqs=82&brandSeqs=280&brandSeqs=293&brandSeqs=296&brandSeqs=300&brandSeqs=299&schStartPrice={schStartPrice}&schEndPrice={schEndPrice}&orderGubun=POPULAR#header"
    #url = f"https://www.officecon.co.kr/product/sales/list?page={i}&schWord=&brandSeqs=51&brandSeqs=35&brandSeqs=267&brandSeqs=62&brandSeqs=164&brandSeqs=36&brandSeqs=38&brandSeqs=63&brandSeqs=93&brandSeqs=168&brandSeqs=37&brandSeqs=255&brandSeqs=254&brandSeqs=251&brandSeqs=242&brandSeqs=241&brandSeqs=178&brandSeqs=71&brandSeqs=69&brandSeqs=60&brandSeqs=39&brandSeqs=34&brandSeqs=32&brandSeqs=281&brandSeqs=282&brandSeqs=294&schPrice2=Y&schStartPrice=&schEndPrice=&orderGubun=POPULAR#header"
    driver.get(url)
    
#     product_list = driver.find_elements(By.CSS_SELECTOR, "div#product_list > ul > li")

#     for j in range(0, len(product_list)) :
#         product_name = driver.find_elements(By.CLASS_NAME, "info02")[j].text
#         # 원가
#         product_price = driver.find_elements(By.CLASS_NAME, "price")[j].text
#         # 할인 가격
#         product_disPrice = driver.find_elements(By.CLASS_NAME, "dis_price")[j].text.split()[1]
#         # 할인율
#         product_percent = driver.find_elements(By.CLASS_NAME, "percent")[j].text
#         # 이미지 src
#         product_image = driver.find_elements(By.CSS_SELECTOR, "div#product_list li figure img")[j].get_attribute('src')
#         # 이미지 이름
#         image_name = now.strftime('%Y%m%d') + "_00" + str(total) + ".jpg"
#         # 이미지 저장
#         urllib.request.urlretrieve(product_image, os.path.join(folder_name, image_name))
#         # 상품 주소
#         product_id = re.search(r'\d+', driver.find_elements(By.CSS_SELECTOR, "div#product_list a")[j].get_attribute('href')).group()
#         product_url = "https://www.officecon.co.kr/product/sales/view?productId="+product_id
#         total += 1

#         #print(product_image)

#         data.append([product_name, product_price, product_disPrice, product_percent, image_name, product_url])

# # pandas DataFrame 생성
# df = pd.DataFrame(data, columns=["상품명", "원가", "할인가", "할인율","상품이미지명", "상품url"])

# # Excel 파일로 저장
# df.to_excel(f"{folder_name}.xlsx", index=False)

time.sleep(3)
