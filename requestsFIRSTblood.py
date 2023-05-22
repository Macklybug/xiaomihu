import requests
url = 'https://www.sogou.com/'
response = requests.get(url=url)
m = response.text
print(m)
with open('./sougou.html', 'w', encoding='utf-8') as fp:
    fp.write(m)
print("./sougou.html完成")