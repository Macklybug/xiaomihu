import requests
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keyword = input("输入keyword：")
pageIndex = eval(input("输入pageIndex："))
pageSize = eval(input("请输入pageSize："))
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 '
                  'Safari/537.36 Edg/113.0.1774.42'
}
parms = {
    'cname': "",
    'pid': "",
    "keyword": keyword,
    'pageIndex': pageIndex,
    'pageSize': pageSize
}
response = requests.post(url=url, params=parms, headers=header)
Post_text = response.text
filename = keyword+'.html'
print(Post_text)
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(Post_text)
print(filename, '保存成功')