import random
import pymysql

db = pymysql.connect(
        host='127.0.0.1', 
        user='root',
        password='1234', 
        db='random_choice', 
        charset='utf8'
)

def random_product() :
    weights = [0.0001, 0.1, 1.4999, 38, 32, 28]
    types = ['X','A','B','C','D','E']
    selected_type = random.choices(types, weights=weights)[0]
    
    cursor = db.cursor()

    sql = f"select * from product where grade = '{selected_type}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result :
        selected_result = random.choice(result)
        result_id           = selected_result[0]
        result_grade        = selected_result[2]
        result_name         = selected_result[3]
        result_price        = selected_result[4]
        result_orgprice     = selected_result[5]
        result_discount  = selected_result[6]
        result_delivery     = selected_result[7]

        sql = "INSERT INTO reward (pno, grade, name, product_price, product_orgprice, discount, delivery) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(result_id, result_grade, result_name, result_price, result_orgprice, result_discount, result_delivery))
        db.commit()
    else :
        print("Not Found Exception")

for i in range(100000) :
    random_product()

    if i > 100000 :
        print('end')