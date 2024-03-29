import pandas as pd
import pymysql
import re

db = pymysql.connect(
        host='127.0.0.1', 
        user='root',
        password='1234', 
        db='random_choice', 
        charset='utf8'
)

cursor = db.cursor()

excel_sheet_1 = pd.read_excel('C:\\Users\\user\\Desktop\\Python\\repos_python\\오피스콘 20240327.xlsx', sheet_name='Sheet1')

boxname             = excel_sheet_1["박스명"]
group_code          = excel_sheet_1["그룹코드"]
group_prob          = excel_sheet_1["그룹확률"]
product_name        = excel_sheet_1["상품명"]
product_price       = excel_sheet_1["원가"]
product_disprice    = excel_sheet_1["할인가"] 
product_discount    = excel_sheet_1["할인율"]



for i in range(len(excel_sheet_1)) :
    product_price_clean = re.sub(r'[^0-9]', '', str(product_price[i]))
    product_disprice_clean = re.sub(r'[^0-9]', '', str(product_disprice[i]))
    product_discount_clean = re.sub(r'[^0-9]', '', str(product_discount[i]))

    sql_insert_1 = f"insert into product \
                                (`boxname`, `group_code`, `group_prob`, `product_name`, `product_price`, `product_disprice`, `discount`, `convert_price`, `delivery`) \
                            values \
                                ('{boxname[i]}', '{group_code[i]}', '{group_prob[i]}', '{product_name[i]}', {product_price_clean}, {product_disprice_clean}, {product_discount_clean}, 3000, 0)"
    
    cursor.execute(sql_insert_1)

db.commit()

cursor.close()
    