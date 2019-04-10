# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('*' * 50)
        print(item['va_name'])
        print(item['ch_number'])
        print(item['ch_name'])
        print(item["ch_link"])
        print(item['ch_content'])
        print("*" * 50)
        return item
