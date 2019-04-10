import requests
import json

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


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
            print(name,score)
        #

    # 保存页面
    def write_page(self):
        pass

    # 主函数
    def work_on(self):
        n = input('请输入要爬取的电影数量')
        params = {'type': "11",
        'interval_id': '100:90',
        'action':'',
        'start': '0',
        'limit': n }
        self.get_page(params)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.work_on()
