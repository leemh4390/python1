import random

x = 3000
total_value = 0

def open_box() :
    probabilities = [0.00064, 0.099, 1.062, 58.83118, 29.993, 10.01418]

    if sum(probabilities) == 100 :
        items       = ['Grand X', 'Grand A', 'Grand B', 'Grand C', 'Grand D', 'Grand E']
        selected_item   = random.choices(items, weights=probabilities, k=1)[0]
        return selected_item

item_info = {  'Grand X': {'count': 0,  'price': 86000000}
             , 'Grand A': {'count': 0,  'price': 8600000}
             , 'Grand B': {'count': 0,  'price': 1700000}
             , 'Grand C': {'count': 0,  'price': 167000}
             , 'Grand D': {'count': 0,  'price': 120000}
             , 'Grand E': {'count': 0,  'price': 105000}}

for i in range(x):
    selected_item = open_box()
    item_info[selected_item]['count'] += 1

for item, info in item_info.items():
    count = info['count']
    price = info['price']
    total_price = count * price
    total_value += total_price
    #print(f"{item} 는 {count} 회 당첨되었습니다.")
    #print(f"총 당첨 금액은 {price * count} 원 입니다.")

print(f"총 이익금 : {x * 100000} 총계: {total_value}")