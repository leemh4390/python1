import random

x = 3000
total_value = 0

def open_box() :
    probabilities = [0.0009, 0.1, 2.0, 18.6254, 28.9746, 50.2991]

    if sum(probabilities) == 100 :
        items       = ['Grand X', 'Grand A', 'Grand B', 'Grand C', 'Grand D', 'Grand E']
        selected_item   = random.choices(items, weights=probabilities, k=1)[0]
        return selected_item

item_info = {  'Grand X': {'count': 0,  'price': 10000000}
             , 'Grand A': {'count': 0,  'price': 1000000}
             , 'Grand B': {'count': 0,  'price': 100000}
             , 'Grand C': {'count': 0,  'price': 20000}
             , 'Grand D': {'count': 0,  'price': 15000}
             , 'Grand E': {'count': 0,  'price': 10000}}

for i in range(x):
    selected_item = open_box()
    item_info[selected_item]['count'] += 1

for item, info in item_info.items():
    count = info['count']
    price = info['price']
    total_price = count * price
    total_value += total_price
    print(f"{item} 는 {count} 회 당첨되었습니다.")
    print(f"총 당첨 금액은 {price * count} 원 입니다.")

print(f"Total Value: {total_value}")