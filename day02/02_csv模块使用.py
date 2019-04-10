import csv

with open('老师.csv','a') as f:
  # 初始化写入对象
  writer = csv.writer(f)
  # 写数据,参数一定为列表
  writer.writerow(['旭叔叔','39'])
  writer.writerow(['魏叔叔','40'])
  writer.writerow(['超哥哥','26'])