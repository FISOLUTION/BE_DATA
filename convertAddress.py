import requests, json
import pandas as pd
import time


def get_location(address):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    # 'KaKaoAK '는 그대로 두시고 개인키만 지우고 입력해 주세요.
    # ex) KakaoAK 6af8d4826f0e56c54bc794fa8a294
    headers = {"Authorization": "KakaoAK 380c8844973349177150873a807bdf38"}
    api_json = json.loads(str(requests.get(url,headers=headers).text))
    #   address = api_json['documents'][0]['address']
    return api_json

def result_location(i):
    api_json = get_location(test_data['address'][i])
    if api_json['documents']:
        address = api_json['documents'][0]['address']
        test_data.loc[i,'x'] = address['x'];
        test_data.loc[i,'y'] = address['y']
    else:
        test_data.loc[i,'x'], test_data.loc[i,'y'] = None, None
    print(i, '번째 변환 완료...')

# -------------------------------------------------------------------
test_data = pd.read_csv('center.csv', encoding='utf-8')

i = 0
while i<=726:
    try:
        result_location(i)
        i+=1
    except:
        print('time.sleep 적용합니다.')
        time.sleep(2)
        result_location(i)
        i+=1

test_data.to_csv('include_xy.csv', encoding='utf-8-sig')