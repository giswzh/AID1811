import requests
import re
import time
import pymysql

class TencentSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

        self.db = pymysql.connect('localhost', 'root', '123456', 'tencent', charset='utf8')
        self.cursor = self.db.cursor()


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

            # 调用获取二级子界面信息
            d1 = self.get_job_detail(job_link)

            d = {
                "职位链接":job_link,
                "职位名称":job_name,
                "职位类型":job_type,
                "招聘人数":job_number,
                "招聘地点":job_address,
                "发布时间":job_time,
                "工作职责":d1["岗位职责"],
                "工作要求":d1["岗位要求"]
            }

            self.write_mysql(d)

    # 获取二级子界面信息
    def get_job_detail(self,job_link):
        res = requests.get(job_link, headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        d1 = self.parse_job_detail(html)
        return d1
    # 解析职位详细信息
    def parse_job_detail(self,html):
        p = re.compile('<tr class="c">.*?<ul class="squareli">(.*?)</ul>',re.S)
        job_detail_list = p.findall(html)
    #     job_detail_list:[('工作职责'),"工作要求"]
    #     job_detail_list = job_detail_str.split('\n')
    #     for job in job_detail_list:
        job_duty = job_detail_list[0].replace("<li>",'').replace("</li>","")
        job_demand = job_detail_list[1].replace("<li>",'').replace("</li>","")
        d1 = {
            "岗位职责":job_duty,
            "岗位要求":job_demand
        }
        return d1


    # 数据存储
    def write_mysql(self,d):
        ins = 'insert into job_info(job_link, job_name, job_type,job_number,\
                    job_address, job_time, job_duty, job_demand) values(%s, %s,%s,\
                    %s, %s, %s, %s, %s)'
        for r_t in d:
            l = [d["职位链接"].strip(),
                 d["职位名称"].strip(),
                 d["职位类型"].strip(),
                 d["招聘人数"].strip(),
                 d["招聘地点"].strip(),
                 d["发布时间"].strip(),
                 d["工作职责"].strip(),
                 d["工作要求"].strip()
                 ]
        self.cursor.execute(ins, l)
        # 提交到数据库执行d
        self.db.commit()

    # 主函数
    def work_on(self):
        for pn in range(30,40, 10):
            url = "https://hr.tencent.com/position.php?&start=%s" %str(pn)
            self.get_job_info(url)
            time.sleep(2)

        #     关闭数据库
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    start = time.time()
    spider = TencentSpider()
    spider.work_on()
    end = time.time()
    print("执行时间:%.2f" %(end - start))