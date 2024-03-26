from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests 
import re
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://biz.giftishow.com/bizshop?price=4500,5000" 
res = requests.get(url) 
res.raise_for_status()
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

try :
    body_element = driver.find_element(By.CSS_SELECTOR,"body")
    body_element.click()
    print(body_element)
except NoSuchElementException:
    print('요소가 없습니다.')

time.sleep(10)
