import requests

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554203356522&di=c49e3006d39ea50bfc28c6b01dfa0c60&imgtype=0&src=http%3A%2F%2Fwww.pptok.com%2Fwp-content%2Fuploads%2F2012%2F08%2Fxunguang-4.jpg"

headers = {'User-Agent':'Mozilla//5.0'}

# 发送请求
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# 获取bytes数据类型
html = res.content

# 写文件
with open('tupian.jpg','wb') as f:
    f.write(html)