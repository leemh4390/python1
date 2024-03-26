import random
import math

item_info = {  
                # 1단계 상품....
                "A1" : {"name" : "[포스트] 아몬드 후레이크", "count" : 0, "price" : 5000, 'discount' : 15},
                "A2" : {"name" : "[홍푸드] 새싹보리 검은콩 미숫가루 스틱", "count" : 0, "price" : 5000, 'discount' : 15},
                "A3" : {"name" : "[한샘] 키친타올걸이", "count" : 0, "price" : 5000, 'discount' : 15},

                # 2단계 상품
                "B1" : {"name" : "[화이트판다] 다크서클 제거 아이크림", "count" : 0, "price" : 5500, 'discount' : 15},
                "B2" : {"name" : "[벨루아체] 수분 콜라겐 링클 멀티밤 10g", "count" : 0, "price" : 5700, 'discount' : 25},
                "B3" : {"name" : "[이지앤] 핸드쿠커 5호 4종", "count" : 0, "price" : 6000, 'discount' : 15},

                # 3단계 상품
                "C1" : {"name" : "[비브르] UV살균 팬건조 칫솔살균기", "count" : 0, "price" : 10000, 'discount' : 15},
                "C2" : {"name" : "[비브르] 에어 선풍기", "count" : 0, "price" : 11000, 'discount' : 15},
                "C3" : {"name" : "[맘스터치] 맘스터치 2만원권", "count" : 0, "price" : 12000, 'discount' : 15},

                # 4단계 상품
                "D1" : {"name" : "[오구펫] 퓨리톤 샴푸 300ml", "count" : 0, "price" : 15000, 'discount' : 15},
                "D2" : {"name" : "[오구펫] 퓨리톤 미슽으 40ml", "count" : 0, "price" : 16000, 'discount' : 15},
                "D3" : {"name" : "[블루원] 석류 어쩌고", "count" : 0, "price" : 17000, 'discount' : 15},

                # 5단계 상품
                "E1" : {"name" : "[셰퍼] 셰퍼112", "count" : 0, "price" : 20000, 'discount' : 15},
                "E2" : {"name" : "[셰퍼] 셰퍼113", "count" : 0, "price" : 23000, 'discount' : 15},
                "E3" : {"name" : "[셰퍼] 셰퍼114", "count" : 0, "price" : 25000, 'discount' : 15},

                # 6단계 상품
                "F1" : {"name" : "6단계 상품1", "count" : 0, "price" : 40000, 'discount' : 15},
                "F2" : {"name" : "6단계 상품2", "count" : 0, "price" : 45000, 'discount' : 15},
                "F3" : {"name" : "6단계 상품3", "count" : 0, "price" : 50000, 'discount' : 15},

                # 7단계 상품
                "G1" : {"name" : "7단계 상품1", "count" : 0, "price" : 100000, 'discount' : 15},
                "G2" : {"name" : "7단계 상품2", "count" : 0, "price" : 110000, 'discount' : 15},
                "G3" : {"name" : "7단계 상품3", "count" : 0, "price" : 120000, 'discount' : 15},

                # 8단계 상품
                "H1" : {"name" : "8단계 상품1", "count" : 0, "price" : 500000, 'discount' : 15},
                "H2" : {"name" : "8단계 상품2", "count" : 0, "price" : 500000, 'discount' : 15},
                "H3" : {"name" : "8단계 상품3", "count" : 0, "price" : 500000, 'discount' : 15},

                # 9단계 상품
                "I1" : {"name" : "9단계 상품1", "count" : 0, "price" : 1000000, 'discount' : 15},
                "I2" : {"name" : "9단계 상품2", "count" : 0, "price" : 1000000, 'discount' : 15},
                "I3" : {"name" : "9단계 상품3", "count" : 0, "price" : 1000000, 'discount' : 15}

}

# 투입 금액
money = 5000 
number = 3000
total_value = 0

def calculate(product) :
    global total_value
    select  = random.choice(product)
    selected_item_info = item_info[select] 
    selected_item_info["count"] += 1
    value = math.trunc(selected_item_info["price"] - selected_item_info["price"] * 20 / 100)
    total_value += value
    #print(select, "name : ", selected_item_info['name'], "count : ", selected_item_info['count']," 회")
    return total_value, selected_item_info

def open_box(money) :
    items = ["1단계 상품", "2단계 상품", "3단계 상품", "4단계 상품", "5단계 상품", "6단계 상품", "7단계 상품", "8단계 상품", "9단계 상품"]
    weights = [93.0041, 4.25, 1.3, 0.8, 0.4, 0.15, 0.09, 0.0049, 0.001]
    selected_item = random.choices(items, weights)[0]
    
    if selected_item == "1단계 상품" :
        product = "A1", "A2", "A3"
    elif selected_item == "2단계 상품" :
        product = "B1", "B2", "B3"
    elif selected_item == "3단계 상품" :
        product = "C1", "C2", "C3"
    elif selected_item == "4단계 상품" :
        product = "D1", "D2", "D3"
    elif selected_item == "5단계 상품" :
        product = "E1", "E2", "E3"
    elif selected_item == "6단계 상품" :
        product = "F1", "F2", "F3"
    elif selected_item == "7단계 상품" :
        product = "G1", "G2", "G3"
    elif selected_item == "8단계 상품" :
        product = "H1", "H2", "H3"
    elif selected_item == "9단계 상품" :
        product = "I1", "I2", "I3"

    calculate(product)     

total_value = 0
for i in range(number) :
    open_box(money)

for item_key, item_value in item_info.items():
    #print(f"{item_key} 상품명: {item_value['name']}, 당첨수 : {item_value['count']}, 가격 : {format(item_value['price'], ',')}")
    print(f"{item_value['count']}")
print("누적된 값:", format(total_value, ','))