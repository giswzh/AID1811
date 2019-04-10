import requests
from lxml import etree
import time
import csv

class qiushiSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        self.proxies = {'http':'http://190.214.26.90:53281',
                        'https':'https://190.214.26.90:53281'}
    # 获取解析页面
    def get_info(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_info(html)
    # 解析信息
    def parse_info(self,html):
        parse_html = etree.HTML(html)
        # 基准xpath://div[@class='article block untagged mb15 typs_hot']
        info_list = parse_html.xpath("//div[@class='article block untagged mb15 typs_hot']|//div[@class='article block untagged mb15 typs_long']")

        # 详细解析:用户昵称,段子内容,好笑数量,评论数量
        for div in info_list:
            user_name = div.xpath('./div[@class="author clearfix"]//h2/text()')[0].strip().replace('\n','')
            content = div.xpath('./a[@class="contentHerf"]/div[@class="content"]/span/text()')
            laugh_count = div.xpath("./div[@class='stats']/span[@class='stats-vote']//i[@class='number']/text()")[0].strip().replace('\n','')
            reply_count = div.xpath("./div[@class='stats']/span[@class='stats-comments']//i[@class='number']/text()")[0].strip().replace('\n','')
            print(user_name)
            print("".join(content).replace("\n",''))
            print(laugh_count,reply_count)
            print("*"*40)
        # for i in range(len(laugh_count)):
        #     r_list = [user_name[i].replace('\n',''),
        #                 laugh_count[i].replace('\n',''), reply_count[i].replace('\n','')]
        #     self.write_csv(r_list)

        # self.write_csv(r_list)
    # 存储数据
    def write_csv(self,r_list):
        with open('qiushi.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow(r_list)
    
    def workon(self):
        for pn in range(1,2):
            url = 'https://www.qiushibaike.com/text/page/%s'%str(pn)
            self.get_info(url)
            time.sleep(2)

if __name__ == '__main__':
    start = time.time()
    qiushi = qiushiSpider()
    qiushi.workon()
    end = time.time()
    print("执行时间:%.2f" %(end - start))
        