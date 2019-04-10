from bs4 import BeautifulSoup

html = '''
<div class="test">风云雄霸天下</div>
<div class="test">聂风</div>
<div class="test2">
    <span>第二梦</span>
</div>
'''
soup = BeautifulSoup(html,'html.parser')
r_list = soup.find_all('div',attrs={'class':'test2'})
for r in r_list:
    # 获取class属性值为test2的div节点下面的span节点文本内容
    print(r.span.string)

# find_all ：找所有,列表
# find     ：找到第一个就返回,节点对象
