from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests 
import re
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

url = "https://luckycatch.cafe24.com/admin/index" 
res = requests.get(url) 
res.raise_for_status()
options = Options()
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

# 로그인 페이지
id_value = driver.find_element(By.CSS_SELECTOR, "input#user_id").send_keys("admin")
pass_valu = driver.find_element(By.CSS_SELECTOR, "input#user_pw").send_keys("1111")
driver.find_element(By.CSS_SELECTOR,"div.col-12 > button.btn.btn-primary.w-100.rounded-pill").click()

# index 페이지에서 자사제품등록 페이지로 이동함
driver.find_element(By.CSS_SELECTOR, "aside#sidebar >  ul#sidebar-nav > li:nth-child(4)").click()

# 제품등록 페이지 이동
driver.find_element(By.CSS_SELECTOR, "main.main > div.pagetitle > nav > div.text-lg-end > input#saveBtn").click()

# 파일 선택 클릭
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys('C:/Users/user/Desktop/Python/repos_python/file/[기획특가]아메리카노 R.jpg')

product_name = driver.find_element(By.CSS_SELECTOR,"input#box_nm").send_keys("[기획특가]아메리카노 R")
product_price = driver.find_element(By.CSS_SELECTOR, "input#price").send_keys("5000")
product_orgprice = driver.find_element(By.CSS_SELECTOR, "input#orig_price").send_keys("3500")
product_delivery = driver.find_element(By.CSS_SELECTOR, "input#delivery_price").send_keys("3000")
time.sleep(2)
product_content = driver.find_element(By.CSS_SELECTOR, "iframe")
driver.switch_to.frame(product_content)
product_information = driver.find_element(By.CSS_SELECTOR, "body")
product_information.send_keys("test..")

time.sleep(5)



