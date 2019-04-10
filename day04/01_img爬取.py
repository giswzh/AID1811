from lxml import etree
import requests
import time

class imgSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    # 获取贴吧页面
    def get_info(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        if len(url) == 35:
            html = res.text
            self.parse_img(html)
        elif url[-4:] =='.jpg':
            # 获取bytes数据类型
            html = res.content
            # 写文件
            jpg_name = url.split('/')[-1]
            with open(jpg_name, 'wb') as f:
                f.write(html)
        else:
            html = res.text
            self.parse_info(html)
    # 解析贴吧页面
    # xpath //div[@class="t_con cleafix"]//a[@class="j_th_tit "]/@href
    def parse_info(self,html):
        parse_html = etree.HTML(html)
        _link = parse_html.xpath("//div[@class='t_con cleafix']//a[@class='j_th_tit ']/@href")
        for i in _link:
            sub_link = "http://tieba.baidu.com" + i
            self.get_info(sub_link)

    # , 获取二级页面
    def get_img(self,url):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parse_img(html)

    # 解析二级页面,获取图片链接
    def parse_img(self,html):
        parse_html = etree.HTML(html)
    # xpath    // div[@class="d_post_content j_d_post_content clearfix"]/img[@class='BDE_Image']/@src
        img_link = parse_html.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')


    # 从图片链接下载图片
        for i in img_link:
            print(i)
            self.get_info(i)

    # 工作函数
    def work_on(self):
        url = "http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&pn=0"
        self.get_info(url)
        time.sleep(2)

if __name__ == '__main__':
    spider = imgSpider()
    spider.work_on()