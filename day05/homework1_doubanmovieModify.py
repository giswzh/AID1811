# -*- coding: UTF-8 -*-
import requests
import json
from selenium import webdriver
import pymysql
import re
from urllib import parse

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.conn = pymysql.connect('localhost','root','123456',charset='utf8')
        self.cursor = self.conn.cursor()

    # 获取页面
    def get_page(self,params):
        res = requests.get(self.url,params=params,headers=self.headers)
        html = res.text
        # html : [{}, {}, {}]
        self.parse_page(html)
    # 解析页面
    def parse_page(self,html):
        #把json格式的字符串转为Python数据类型
        r_list = json.loads(html)
        for r in r_list:
            name = r['title']
            score = r['score']
            print(r)
        #

    # 保存页面
    def write_page(self,r_list):
        ins = 'insert into top100(name, star, time) values(%s, %s, %s)'
        for r_t in r_list:
            l = [r_t[0].strip(),
                 r_t[1].strip(),
                 r_t[2].strip()[5:15]
                 ]
            self.cursor.execute(ins, l)
            # 提交到数据库执行d
            self.db.commit()

    # 主函数
    def work_on(self):
        driver = webdriver.PhantomJS()
        driver.get("https://movie.douban.com/chart")
        # display_types = driver.find_elements_by_xpath(xpath="//div[@class='types']//a/@href")

        # 这里获取电影类型与每个类型的编号并生成字典d
        display_types = driver.find_elements_by_xpath(xpath='//*[@id="content"]/div/div[2]/div[1]/div/span/a')
        d = {}
        for i in display_types:
            s = i.get_attribute('href')
            l =  re.findall('.*=(.*)&.*.*=(.*)&.*.*=(.*)&.*',s)[0]
            s_type = parse.unquote(l[0])
            print(s_type,l[1])
            print("*"*50)
            d[s_type] = l[1]
        print(d)

        input_type = input('请输入要爬取的类型')
        n = input('请输入要爬取的电影数量')
        if input_type in d:
            params = {'type': d[input_type],
                      'interval_id': '100:90',
                      'action':'',
                      'start': '0',
                      'limit': n }
        self.get_page(params)

        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.work_on()
