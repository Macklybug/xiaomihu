import json

import requests
post_url = "https://fanyi.baidu.com/sug"
#post请求参数处理（同get请求一致）
word = input("enter a world")
data = {
    'kw': word
}
#进行UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 Edg/113.0.1774.42'
}

#请求发送(注意是headers,而不是header)
response = requests.post(url=post_url, data=data, headers=header)
#获取想要数据,jaon方法返回一个对象（如果确认想要数据是json类型，才用该方法）
dic_obj = response.json()
#进行持久化存储
fileName = word+".json"
fp = open(fileName, 'w', encoding='utf-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
print('Over ')
