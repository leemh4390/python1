import pandas as pd
import pymysql

db = pymysql.connect(
        host='127.0.0.1', 
        user='root',
        password='1234', 
        db='random_choice', 
        charset='utf8'
)

cursor = db.cursor()

excel_sheet_1 = pd.read_excel('C:\\Users\\user\\Desktop\\Python\\product.xlsx', sheet_name='Sheet1')

grade               = excel_sheet_1["등급"]
product_name        = excel_sheet_1["상품명"]
# 소비자가격
product_price       = excel_sheet_1["가격"] 
# 원가
product_orgprice    = excel_sheet_1["구매가"] 
product_discount    = excel_sheet_1["할인율"]
# 포인트 전환 금액
product_convert     = excel_sheet_1["포인트"] 
delivery            = excel_sheet_1["배송비"]

print(product_convert)


for i in range(len(excel_sheet_1)) :
    sql_insert_1 = f"insert into product \
                                (`boxname`, `grade`, `product_name`, `product_price`, `org_price`, `discount`, `convert_price`, `delivery`) \
                            values \
                                ('bronzebox', '{grade[i]}', '{product_name[i]}', {product_price[i]}, {product_orgprice[i]}, {product_discount[i]}, {product_convert[i]}, {delivery[i]})"
    
    cursor.execute(sql_insert_1)

db.commit()

cursor.close()
    