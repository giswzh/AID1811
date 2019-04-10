import requests
import re
import time

class TencentSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}



    # 获取一级子界面职位信息
    def get_job_info(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
    #     交给解析函数去做解析
        self.parse_job_infor(html)

    # 解析职位信息
    def parse_job_infor(self,html):
        p = re.compile('<td class="l square">.*?href="(.*?)">(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
        job_info_list = p.findall(html)
    #     job_info_list:[('链接','名称','类别','人数','地点',''),(),(),(),()]
        for job in job_info_list:
            job_link = "https://hr.tencent.com/" + job[0]
            job_name = job[1]
            job_type = job[2]
            job_number = job[3]
            job_address = job[4]
            job_time = job[5]

            d = {
                "职位链接":job_link,
                "职位名称":job_name,
                "职位类型":job_type,
                "招聘人数":job_number,
                "招聘地点":job_address,
                "发布时间":job_time
            }

            print(d)
            print("*" * 30)


    # 数据存储
    def write_page(self):
        pass


    # 主函数
    def work_on(self):
        for pn in range(0, 10, 10):
            url = "https://hr.tencent.com/position.php?&start=%s" %str(pn)
            self.get_job_info(url)
            time.sleep(2)

if __name__ == '__main__':
    start = time.time()
    spider = TencentSpider()
    spider.work_on()
    end = time.time()
    print("执行时间:%.2f" %(end - start))