# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib import request
import re
import time
import csv
import pymongo
class MaoyanSpider(object):
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    # 用来计数
    self.page = 1

  # 获取页面
  def get_page(self,url):
    req = request.Request(url,headers=self.headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 直接调用解析函数,去对html做解析
    self.parse_page(html)

  # 解析页面
  def parse_page(self,html):
    p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?time">(.*?)</p>',re.S)
    r_list = p.findall(html)
    # r_list:[('霸王别姬','张国荣','1993-4-1'),(),()]
    # 直接调用保存数据函数
    self.write_mongo(r_list)

  # 保存数据
    # 保存数据
    def write_mongo(self, r_list):
        for r_t in r_list:
            d = {'电影名称': r_t[0].strip(),
                 '电影主演': r_t[1].strip(),
                 '上映时间': r_t[2].strip()
                 }
            self.myset.insert_one(d)

  # 主函数
  def work_on(self):
    for pn in range(0,41,10):
      url = 'https://maoyan.com/board/4?offset=%s'\
                                          % str(pn)
      self.get_page(url)
      print('第%d页爬取成功' % self.page)
      self.page += 1
      time.sleep(2)


if __name__ == '__main__':
  begin = time.time()
  spider = MaoyanSpider()
  spider.work_on()
  end = time.time()
  print('执行时间:%.2f' % (end-begin))








     # 解析页面
    def parse_page(	self, html):
        p = re.compile('', re.S)
        r_list = p.findall(html)
        # r_list:[(),(),()]
        # 直接调用保存数据的函数
        self.write_mongo(r_list)

