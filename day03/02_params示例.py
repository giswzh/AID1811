import requests

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
key = input('请输入要搜索的内容')
params = {
    'wd':key,
    'pn':'10'
}
url = 'https://www.baidu.com/s?'

#三步走,自动对params编码,后和基准url进行拼接
res = requests.get(url,params=params, headers=headers)
res.encoding = 'utf-8'
html = res.text

print(html)
