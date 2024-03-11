import requests 
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://hashbox.monster/goods/detail/1" 
res = requests.get(url) 
res.raise_for_status()
soup = BeautifulSoup(res.content, "html.parser")

def information() :
    elements  = soup.select("div.product_guide > div.item_rank")
    data = []
    discount = 0
    value1 = 'ground_b'
    value2 = 'ground_normal'  

    for element in elements :
        title = element.find('div','title_information suit_medium_font').text.strip()
        price = element.find('div','price_information suit_bold_font').find('spna').text.strip()
        probability = 0.0001
        if title and price == None :
            continue
        data.append([title, price, discount,probability]) 

    elements = soup.select(f"div.product_guide > div.item_rank_all_box > div.small_box.{value1}")
    for element in elements :
        title = element.get('title')
        price = element.find('div','price_num')
        probability = 3.23

        if title and price :
            price = price.text.strip()
        else : 
            continue
        data.append([title, price, discount,probability]) 

    elements = soup.select(f"div.product_guide > div.item_rank_all_box > div.small_box.{value2}")
    for element in elements :
        title = element.get('title')
        price = element.find('div','price_num')
        probability = 1.43

        if title and price :
            price = price.text.strip()
        else : 
            continue
        data.append([title, price, discount, probability]) 
    return data

# 데이터 가져오기
data = information()

print(data)

# pandas DataFrame 생성
df = pd.DataFrame(data, columns=["상품명", "가격", "할인율", "당첨확률"])

# Excel 파일로 저장
df.to_excel("hashboxmonster.xlsx", index=False)