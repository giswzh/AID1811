from lxml import etree
import requests
import time

class houseSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    # 获取页面
    def get_info(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_info(html)

    # 解析页面
    def parse_info(self,html):
        parse_html = etree.HTML(html)
        r_general = parse_html.xpath('//div[@class="content__list--item"]')
        for r in r_general:
            pass
    #链接, ./a[@class="content__list--item--aside"]/@href
    # 标题    ./p[@class="content__list--item--title twoline"]/a
    #位置     ./p[@class="content__list--item--des"]/a[1]
    #
    #
    #
    #
    #
    #
    #
    #
    # ,

    # 存入数据
    def write_csv(self,r_list):
        pass

    # 执行函数
    def work_on(self):
        for i in range(1,101):
            url = 'https://bj.lianjia.com/zufang/pg100/pg%s' %str(i)
            self.get_info(url)
            time.sleep(2)

if __name__ == '__main__':
    hspider = houseSpider()
    hspider.work_on()