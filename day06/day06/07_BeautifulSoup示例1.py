from bs4 import BeautifulSoup

html = '''<div class="test">风云雄霸天下</div>'''
soup = BeautifulSoup(html,'lxml')
r_list = soup.find_all('div',attrs={'class':'test'})
for r in r_list:
    print(r.text)
    print(r.get_text())



