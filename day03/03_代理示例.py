import requests


url = 'https://whatismyip.com'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

proxies = {"https":'https://190.214.26.90:53281',
           "http":"http://190.214.26.90:53281"}

# proxies = {"https":'https://309435365:szayclhp@116.255.191.105:16816"',
#            "http":"http://309435365:szayclhp@116.255.191.105:16816"}

# 发请求:
res = requests.get(url,headers=headers,proxies=proxies)
res.encoding = 'utf-8'
html = res.text
print(html)