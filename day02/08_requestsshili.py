import requests

#常用变量
url = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla//5.0'}
#发请求获取响应内容
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text
#查看字符编码
# print(res.encoding)
print(html)
# 获取bytes数据类型
print(type(res.content))
# http响应码
print(res.status_code)