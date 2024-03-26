from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import openpyxl
import math
import urllib
import urllib.request
import os

# 작성자 : 이민혁
# 날짜 : 2024/02/28
# 최종 수정일 : 2024/02/28
# 오피스콘 카테고리에 맞는 목록을 엑셀로 만들어줍니다.

# 사진이 저장되는 폴더명
folder_name = "officecon"

# 폴더가 없으면 만듬
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
        
# 엑셀 생성
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["브랜드", "상품명", "사진명", "가격", "상품내용", "할인가", "할인율", "상품링크", "최소수량"])

# 커피/음료 1 
# 베이커리/디저트 2
# 아이스크림 3
# 배달 이용권 4
# 치킨/피자/버거 5
# 외식 6
# 편의점/마트 7
# 금액권 8
# 상품권 9
# 주유/차량정비 10
# 뷰티/헬스 11
# 문화/교육 12

# 상단에 있는 물건 코드를 xfilename 에 입력하면 할인 금액이 6% 미만인 제품은 제외하고 엑셀 파일이 생성됩니다.
# 기획 상품은 사용자가 엑셀 파일 열어서 직접 제거해야함
xlfilename = "1"

# 시작 페이지
startNum = 1 
# 종료 페이지
endNum = 20

# 금액 범위
startPrice  = 5000 # 최소 금액
endPrice    = 10000 # 최대 금액

# 상품 url 은 여기서 수정하면 됩니다.
urlschWord_mapping = {
    "1": "&schWord=&brandSeqs=239&brandSeqs=50&brandSeqs=48&brandSeqs=49&brandSeqs=279&brandSeqs=259&brandSeqs=256&brandSeqs=245&brandSeqs=231&brandSeqs=225&brandSeqs=215&brandSeqs=214&brandSeqs=200&brandSeqs=179&brandSeqs=116&brandSeqs=81&brandSeqs=61&brandSeqs=58&brandSeqs=54&brandSeqs=53&brandSeqs=46&brandSeqs=44&brandSeqs=43&brandSeqs=82&brandSeqs=280&brandSeqs=293&",
    "2": "&schWord=&brandSeqs=10&brandSeqs=9&brandSeqs=287&brandSeqs=249&brandSeqs=226&brandSeqs=221&brandSeqs=119&brandSeqs=117&brandSeqs=99&brandSeqs=67&brandSeqs=8&brandSeqs=7&brandSeqs=6&brandSeqs=278&brandSeqs=218&brandSeqs=284&brandSeqs=114&",
    "3": "&schWord=&brandSeqs=41&brandSeqs=97&",
    "4": "&schWord=&brandSeqs=202&brandSeqs=159&brandSeqs=149&",
    "5": "&schWord=&brandSeqs=51&brandSeqs=35&brandSeqs=267&brandSeqs=62&brandSeqs=164&brandSeqs=36&brandSeqs=38&brandSeqs=63&brandSeqs=93&brandSeqs=168&brandSeqs=37&brandSeqs=255&brandSeqs=254&brandSeqs=251&brandSeqs=242&brandSeqs=241&brandSeqs=178&brandSeqs=71&brandSeqs=69&brandSeqs=60&brandSeqs=39&brandSeqs=34&brandSeqs=32&brandSeqs=281&brandSeqs=282&brandSeqs=294&",
    "6": "&schWord=&brandSeqs=134&brandSeqs=31&brandSeqs=23&brandSeqs=22&brandSeqs=290&brandSeqs=289&brandSeqs=286&brandSeqs=260&brandSeqs=253&brandSeqs=250&brandSeqs=248&brandSeqs=243&brandSeqs=229&brandSeqs=222&brandSeqs=216&brandSeqs=181&brandSeqs=171&brandSeqs=163&brandSeqs=160&brandSeqs=147&brandSeqs=143&brandSeqs=142&brandSeqs=108&brandSeqs=95&brandSeqs=68&brandSeqs=56&brandSeqs=29&brandSeqs=25&brandSeqs=224&brandSeqs=223&brandSeqs=20&brandSeqs=269&brandSeqs=211&",
    "7": "&schWord=&brandSeqs=11&brandSeqs=244&brandSeqs=57&brandSeqs=12&",
    "8": "&schWord=&brandSeqs=258&brandSeqs=59&brandSeqs=140&brandSeqs=13&brandSeqs=288&brandSeqs=285&",
    "9": "&schWord=&brandSeqs=18&brandSeqs=165&brandSeqs=192&brandSeqs=213&brandSeqs=204&brandSeqs=170&brandSeqs=141&brandSeqs=73&brandSeqs=70&brandSeqs=64&brandSeqs=17&brandSeqs=14&brandSeqs=292&",
    "10": "&schWord=&brandSeqs=166&brandSeqs=16&",
    "11": "&schWord=&brandSeqs=3&brandSeqs=169&brandSeqs=153&",
    "12": "&schWord=&brandSeqs=52&brandSeqs=5&brandSeqs=4&brandSeqs=262&brandSeqs=295&"    
}

if xlfilename in urlschWord_mapping :
    urlschWord      = urlschWord_mapping[xlfilename]

img_list = []

for i in range(startNum, endNum + 1) :
    urlPage         = "https://www.officecon.co.kr/product/sales/list?page="+str(i)
    urlschPrice     = "schStartPrice="+str(startPrice)+"&schEndPrice="+str(endPrice)+"&orderGubun=POPULAR#header"
    url             = urlPage + urlschWord + urlschPrice
    res             = requests.get(url)
    soup            = BeautifulSoup(res.content, 'html.parser')
    items           = soup.select("#product_list > ul > li")

    for item in items: 
        brandType               = item.select_one("p.info01").get_text(strip=True)[0:1]
        brandName               = item.select_one("p.info01").get_text(strip=True)[1:]
        productName             = item.select_one("p.info02").get_text(strip=True)
        price_element           = item.select_one("span.price")
        product_code            = item.select_one("button").attrs['onclick']
        discountRate_element    = item.select_one("strong.percent")
        product_url             = "https://www.officecon.co.kr/product/sales/view?productId=" + product_code.split('Id=',1)[1].strip("'); return false;") + "#header"
        
        base_url = "https://www.officecon.co.kr"
        img_src = item.select_one('img').get('src')

        url = base_url + img_src
        img_list.append(url)
        for i in range(0, len(img_list)) : 
            try : 
                # 이미지 저장하는 코드
                main_img = os.path.join(folder_name,"n_" + productName + ".jpg")
                urllib.request.urlretrieve(img_list[i],filename=main_img)
            except :
                continue

        if price_element :
            orgPrice = int(re.sub(r'[^\d]+', '', price_element.get_text(strip=True))) 
        else :
            continue

        if discountRate_element :
            discountRate = int(re.search(r'\d+', discountRate_element.get_text(strip=True)).group())
            if discountRate < 6 :
                continue
        else :
            continue
        main_img_name = "n_" + productName + ".jpg"

        disPrice = round(orgPrice - orgPrice * (discountRate / 100),-1)  # 할인된 가격 계산
        
        sheet.append([brandName, productName, main_img_name, orgPrice, "" ,disPrice, discountRate, product_url])


    
# 엑셀 파일명
filename_mapping = {
    "1": "cafe.xlsx",
    "2": "bakery.xlsx",
    "3": "icecream.xlsx",
    "4": "giftcard.xlsx",
    "5": "chicken.xlsx",
    "6": "out.xlsx",
    "7": "convenience.xlsx",
    "8": "moneycard.xlsx",
    "9": "culture.xlsx",
    "10": "oiling.xlsx",
    "11": "beauty.xlsx",
    "12": "educate.xlsx"
}

# 상단에 있는 xfilename 과 매핑시켜서 엑셀 파일명으로 생성함
if xlfilename in filename_mapping:
    wb.save(filename_mapping[xlfilename])                               

