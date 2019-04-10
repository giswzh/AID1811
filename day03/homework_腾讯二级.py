import requests
from lxml import etree
import time
import pymysql
import csv

class TencentSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

        # self.db = pymysql.connect('localhost', 'root', '123456', 'tencent', charset='utf8')
        # self.cursor = self.db.cursor()


    # 获取一级子界面职位信息
    def get_job_info(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
    #     交给解析函数去做解析
        self.parse_job_infor(html)

    #     将数据

    # 解析职位信息
    def parse_job_infor(self,html):
    #     创建解析对象
        parse_html = etree.HTML(html)

    #     基准xpath
        job_info_list = parse_html.xpath('//tr[@class="odd"]|//tr[@class="even"]')

        for tr in job_info_list:
            job_link = "https://hr.tencent.com/" + tr.xpath("./td[1]/a/@href")[0]
            job_name = tr.xpath("./td[1]/a/text()")[0]
            # job_type = tr.xpath("./td[2]/a/text()")[0]
            # job_number = tr.xpath("./td[3]/a/text()")[0]
            # job_address = tr.xpath("./td[4]/a/text()")[0]
            # job_time = tr.xpath("./td[5]/a/text()")[0]
            print(job_link,job_name)
            self.get_job_detail(job_link)
            print("*" * 40)

    # 获取二级子界面信息
    def get_job_detail(self,job_link):
        res = requests.get(job_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_job_detail(html)
    # 解析职位详细信息
    def parse_job_detail(self,html):
        parse_html = etree.HTML(html)
        job_duty = parse_html.xpath('//tr[@class="c"][1]//ul[@class="squareli"]/li/text()')
        job_demand = parse_html.xpath('//tr[@class="c"][2]//ul[@class="squareli"]/li/text()')
        duty = ''.join(job_duty)
        demand = "".join(job_demand)
        print(duty)
        print(demand)

    # 数据存储
    # def write_mysql(self,d):
    #     ins = 'insert into job_info(job_link, job_name, job_type,job_number,\
    #                 job_address, job_time, job_duty, job_demand) values(%s, %s,%s,\
    #                 %s, %s, %s, %s, %s)'
    #     for r_t in d:
    #         l = [d["职位链接"].strip(),
    #              d["职位名称"].strip(),
    #              d["职位类型"].strip(),
    #              d["招聘人数"].strip(),
    #              d["招聘地点"].strip(),
    #              d["发布时间"].strip(),
    #              d["工作职责"].strip(),
    #              d["工作要求"].strip()
    #              ]
    #     self.cursor.execute(ins, l)
    #     # 提交到数据库执行d
    #     self.db.commit()
    def write_csv(self,r_list):
        with open('zhaopin.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow(r_list)



    # 主函数
    def work_on(self):
        for pn in range(30,40, 10):
            url = "https://hr.tencent.com/position.php?&start=%s" %str(pn)
            self.get_job_info(url)
            time.sleep(2)

        #     关闭数据库
        # self.cursor.close()
        # self.db.close()

if __name__ == '__main__':
    start = time.time()
    spider = TencentSpider()
    spider.work_on()
    end = time.time()
    print("执行时间:%.2f" %(end - start))