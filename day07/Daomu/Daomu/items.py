# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # 卷名
    va_name = scrapy.Field()
    # 章节数量
    ch_number = scrapy.Field()
    #  章节名称
    ch_name = scrapy.Field()
    #   章节链接
    ch_link = scrapy.Field()
    #   小说内容
    ch_content = scrapy.Field()
