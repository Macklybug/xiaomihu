import json

import requests
url = 'https://movie.douban.com/j/chart/top_list'
parm ={
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '1',#从库中第几部电影去取
    'limit': '20'#一次取的值
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 Edg/113.0.1774.42'
}
response = requests.get(url=url, params=parm, headers=header)
list_data = response.json()
fp = open('./douban.json', 'w', encoding='utf-8')
json.dump(list_data, fp=fp, ensure_ascii=False)
print('Over')