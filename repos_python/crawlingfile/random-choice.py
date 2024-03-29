import random
import pymysql

db = pymysql.connect(
        host='127.0.0.1', 
        user='root',
        password='1234', 
        db='random_choice', 
        charset='utf8'
)

cursor = db.cursor()

def random_product() :
    # 확률
    code_weights = [90, 10]
    # 그룹코드
    code_types = ['Gift', 'Point']
    selected_type = random.choices(code_types, code_weights)[0]
    print(selected_type)
    # 기프트가 당첨됐을때
    if selected_type == 'Gift':
        # 확률
        prob_weights = [88, 6, 3, 2, 1]
        #그룹확률
        prob_types = ['GiftA','GiftB', 'GiftC', 'GiftD', 'GiftE']
        selected_group = random.choices(prob_types, prob_weights)[0]
        sql = f"select * from `product` where `group_code` = '{selected_type}' and `group_prob` = '{selected_group}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    # Point 가 당첨
    else :
        sql = f"select * from `product` where `group_code` = '{selected_type}' and `group_prob` = 'PointA'"
        cursor.execute(sql)
        result = cursor.fetchall()     
        return result
    
for i in range(99900) :
    result = random_product()
    if result :
        selected_result = random.choice(result)
        print(selected_result)
        selected_productid          = selected_result[0]
        selected_boxname            = selected_result[1]
        selected_groupcode          = selected_result[2]
        selected_groupprob          = selected_result[3]
        selected_productname        = selected_result[4]
        selected_productprice       = selected_result[5]
        selected_productdisprice    = selected_result[6]
        selected_productdiscount    = selected_result[7]
        selected_convert            = selected_result[8]
        selected_delivery           = selected_result[9]

        print("selected_productname : ", selected_productname, ", selected_productprice : ", selected_productprice)

        sql = "INSERT INTO reward (pno, boxname, group_code, group_prob, name, product_price, product_disprice, discount, convert_price, delivery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(selected_productid, selected_boxname, selected_groupcode, selected_groupprob, selected_productname, selected_productprice, selected_productdisprice, selected_productdiscount, selected_convert, selected_delivery))
        db.commit()    

      
