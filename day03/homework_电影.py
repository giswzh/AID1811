import requests
from lxml import etree
import time
import csv

class movieSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        # self.proxies = {'http':'http://190.214.26.90:53281',
        #                 'https':'https://190.214.26.90:53281'}
        # self.params = {
        #     'offset':params  
        # }
    # 获取解析页面
    def get_info(self,url,params):
        res = requests.get(url,params, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parse_info(html)

    # 进行解析
    def parse_info(self,html):
        parse_htmle = etree.HTML(html)
        c1 = parse_htmle.xpath("//div[@class='movie-item-info']//p[@class='name']/a/text()")
        c2 = parse_htmle.xpath("//div[@class='movie-item-info']//p[@class='star']/text()")
        c3 = parse_htmle.xpath("//div[@class='movie-item-info']//p[@class='releasetime']/text()")
        for i in range(len(c1)):
            r_list = [c1[i].replace('\n',''), 
                        c2[i].replace('\n',''), c3[i].replace('\n','')]
            self.write_csv(r_list)       

    # 数据存储
    def write_csv(self,r_list):
        with open('movie.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow(r_list)

    # 主函数
    def workon(self):
        for pn in range(0,21,10):
            params = {
            'offset':str(pn)  
            }
            url = 'https://maoyan.com/board/4?'
            self.get_info(url,params)
            time.sleep(2)
        
if __name__ == '__main__':
    spider = movieSpider()
    spider.workon()
    