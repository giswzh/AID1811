import requests
import re
import csv
class noteSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

        self.proxies = {"https": 'https://190.214.26.90:53281',
                   "http": "http://190.214.26.90:53281"}
        # web客户端验证参数
        self.auth = ('tarenacode','code_2013')

    # 获取解析页面
    def get_page(self, url):
        res = requests.get(url, auth = self.auth,proxies=self.proxies, headers = self.headers)
        res.encoding = 'utf-8'
        html = res.text

        #解析页面
        p = re.compile('<a href="(.*?)/".*?</a>', re.S)
        r_list = p.findall(html)
        self.write_page(r_list)

    # 保存数据
    def write_page(self, r_list):
        with open("Note.csv","w") as f:
            writer = csv.writer(f)
            for r in r_list:
                if r != "..":
                    writer.writerow([r])

if __name__ == '__main__':
    spider = noteSpider()
    spider.get_page('http://code.tarena.com.cn')