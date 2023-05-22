#ua伪装：（反扒机制）
#UA:User-Agent(请求载体身份标识）
#UA伪装：门户网站的服务器为检测请求载体的标识身份，如果检测到请求载体的身份标识为某一款浏览器
#说明该请求是一个正常请求。但是，如果检测到请求载体的身份标识不是某一款浏览器，则表示该请求为
#不正常请求（爬虫），服务器可能会拒绝请求。

#UA伪装：让爬虫对应的请求载体身份标识伪装成一款浏览器

import requests
#UA伪装方法：将对应的User-Agent封装到一个字典中
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'
}
url = 'https://www.sogou.com/web'
#处理url里的参数：封装到字典里
kw = input("录入关键值")
param = {
        'query': kw
}
#对指定的url发起的请求是携带参数的，并且请求过程中处理了参数
response = requests.get(url=url, params=param, headers=headers)
page_text = response.text
filename = kw+'.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(filename, '保存成功')