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
    weights = [0.0001, 0.002, 0.006, 2, 5, 93]
    types = ['Ground X', 'Ground A', 'Ground B', 'Ground C', 'Ground D', 'Ground E']
    selected_type = random.choices(types, weights=weights)[0]

    cursor = db.cursor()

    sql = f"select * from product where ptype = '{selected_type}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    if result :
        selected_result = random.choice(result)
        result_id       = selected_result[0]
        result_type     = selected_result[1]
        result_name     = selected_result[3]
        result_price    = selected_result[4]
        result_discount = selected_result[5]
        print(result_id, result_type,result_name, result_price)

        sql = "INSERT INTO reward (pno, ptype, pname, price, discount) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(result_id, result_type, result_name, result_price, result_discount))
        db.commit()
    else :
        print("Not Found Exception")

for i in range(100000) :
    random_product()