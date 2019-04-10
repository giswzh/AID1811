# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem
import time

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 一级页面解析,获取所有小说的链接
    def parse(self, response):
        # 盗墓笔记全集链接列表['http://...','http://...']
        one_links_list = response.xpath('//ul[@class="sub-menu"]//a/@href').extract()
        print(one_links_list)
        # 把链接交给调度器入队列
        for one_link in one_links_list:
            yield scrapy.Request(
                        one_link,
                        callback=self.parse_two_link
                )

    # 解析二级页面方法
    def parse_two_link(self,response):
        # 基准xpath,匹配所有节点对象的列表
        article_list = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for article in article_list:
            # 创建item对象
            item = DaomuItem()
            info = article.xpath('./a/text()')\
                                    .extract()[0].split()
            print(info)
            # info:['七星鲁王','第一章,'血尸']
            item['va_name'] = info[0]
            item['ch_number'] = info[1]
            item['ch_name'] = info[2] if len(info) > 2 else ""
            item['ch_link'] = article.xpath('./a/@href')\
                                        .extract()[0]
            # 将章节链接交给调度器
            # 必须把item传递到下一个函数,利用meta参数
            yield scrapy.Request(
                item['ch_link'],
                meta={'item':item},
                callback=self.parse_three_link
            )
            time.sleep(2)
    # 解析三级页面
    def parse_three_link(self,response):
        item = response.meta['item']
        content = response.xpath('//article[@class="article-content"]/p/text()').extract()
        content = '\n'.join(content)
        item['ch_content'] = content

        yield item













