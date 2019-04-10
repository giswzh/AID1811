import requests



# 第一步
post_url = "http://www.renren.com/PLogin.do"
data = {'email':'dxziqin@126.com','password':''}

session = requests.session()

# 第二步
url = 'http://www.renren.com/262225753/profile'
res = session.get(url,headers=headers)
res.encoding = 'utf-8'
print(res.text)