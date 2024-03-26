import random
import math

x = 100000
total_value = 0

def open_box() :
    probabilities = [0.0002, 0.1, 2.0, 57.8998, 30, 10]

    if sum(probabilities) == 100 :
        items       = ['Grand X', 'Grand A', 'Grand B', 'Grand C', 'Grand D', 'Grand E']
        selected_item   = random.choices(items, weights=probabilities, k=1)[0]
        return selected_item

item_info = {  
               'Grand X': {'count': 0,  'price': 1000000, 'discount' : 6}
               # Grand X 는 제일 좋은 상품 할인율을 어떻게 설정해야할지?
             , 'Grand A': {'count': 0,  'price': 100000,  'discount' : 10}
             , 'Grand B': {'count': 0,  'price': 50000,   'discount' : 50}
             , 'Grand C': {'count': 0,  'price': 10000,   'discount' : 70}
                # 제일 당첨 확률이 높은 상품이지만 매입가가 저렴한 상품
             , 'Grand D': {'count': 0,  'price': 7000,    'discount' : 30}
             , 'Grand E': {'count': 0,  'price': 5000,    'discount' : 15}
             }

for i in range(x):
    selected_item = open_box()
    item_info[selected_item]['count'] += 1

for item, info in item_info.items():
    count       = info['count']
    price       = info['price']
    discount    = info['discount']
    total_price = count * (price - price * discount/100)
    total_value += total_price
    print(f"{item} 는 {count} 회 당첨되었습니다.")
    #print(f"총 당첨 금액은 {math.trunc(count * (price - price * discount/100)):,} 원 입니다.")


print(f"총 이익금 : {x * 5000:,}원 총계: {math.trunc(total_value):,}원")