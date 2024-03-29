import requests
import json

url = "https://specialoffer.kr/api/goods"
authorization = "dae7503a65031cdb76cbdd4453de4f481f30a6e57ba9778e87e0a8f7a95e5c10"

headers = {
    "Authorization": f"Bearer {authorization}"
}

params = {
    "page": 1,
    "per_page": 15,
    "category_code" : 521503110,
    "seller_code" : "SC00005684"
}


response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    # 여기서 데이터 처리
    pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
    print(pretty_json)

else:
    print("요청 실패:", response.status_code)    