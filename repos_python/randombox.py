import random

x = int(input('몇 번 뽑으시겠습니까?'))

def open_box() :
    probabilities = [0.45, 0.35, 0.17,0.02, 0.01]

    if sum(probabilities) == 1 :
        items = ['5000원', '5500원', '6000원', '8000원', '10000원']

        selected_item = random.choices(items, weights=probabilities, k=1)[0]

        return selected_item
    else :
        print('확률 설정 요망!')

for i in range(x) :
    selected_item = open_box()
    print(selected_item)
  