from hashlib import md5

key = input('请输入要翻译的单词:')

# 加密三步骤
# 1.创建加密对象
pwdobj = md5()
# 2.进行加密(参数必须为bytes数据类型)
pwdobj.update(key.encode('utf-8'))
# 3.获取十六进制加密结果
sign = pwdobj.hexdigest()

print(sign)




















