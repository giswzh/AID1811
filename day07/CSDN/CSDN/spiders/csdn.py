# -*- coding: utf-8 -*-
import scrapy
from CSDN.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/narci/article/details/776787']

    def parse(selkkf, response):
        #创建item对象
        item = CsdnItem()
        item['title'] = response.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[1]/h1').extract()[0]
        item['time'] = response.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[1]/span[1]').extract()[0]
        item['number'] = response.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[1]/span[2]').extract()[0]
        #把item交给了管道文件
        yield item

