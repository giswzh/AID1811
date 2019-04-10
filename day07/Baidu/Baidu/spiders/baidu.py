# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名(运行爬虫项目时使用)
    name = 'baidu'
    # 允许爬取的域名
    allowed_domains = ['www.baidu.com']
    # 第一个要爬取的url地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print("*" * 50)
        with open('baidu.html','w') as f:
            f.write(response.text)
        print("*" * 50)
