from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import openpyxl
import math
        
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["브랜드", "상품명", "원가","할인가", "할인율"])

#시작 페이지
startNum = 1 
# 종료 페이지
endNum = 1
#금액 범위
startPrice  = 5000
endPrice    = 10000

for i in range(startNum, endNum + 1) :
    urlPage         = "https://www.officecon.co.kr/product/sales/list?page="+str(i)
    urlschWord      = "&schWord=&brandSeqs=3&brandSeqs=169&brandSeqs=153&"
    urlschPrice     = "schStartPrice="+str(startPrice)+"&schEndPrice="+str(endPrice)+"&orderGubun=POPULAR#header"
    url     = urlPage + urlschWord + urlschPrice
    res     = requests.get(url)
    soup    = BeautifulSoup(res.content, 'html.parser')
    items = soup.select("#product_list > ul > li")

    #print(urlPage)

    for item in items: 
        brandType       = item.select_one("p.info01").get_text(strip=True)[0:1]
        brandName       = item.select_one("p.info01").get_text(strip=True)[1:]
        productName     = item.select_one("p.info02").get_text(strip=True)
        price_element = item.select_one("span.price")
        orgPrice = int(re.sub(r'[^\d]+', '', price_element.get_text(strip=True))) if price_element else 0

        discountRate_element = item.select_one("strong.percent")
        discountRate = int(re.search(r'\d+', discountRate_element.get_text(strip=True)).group()) if discountRate_element else 0

        disPrice = round(orgPrice - orgPrice * (discountRate / 100),-1)  # 할인된 가격 계산
        sheet.append([brandName, productName, orgPrice, disPrice, discountRate])
    
# 6. 수집한 데이터 저장
wb.save("beauty.xlsx")


           











