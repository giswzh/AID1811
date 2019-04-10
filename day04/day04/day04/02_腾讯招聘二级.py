import requests
from lxml import etree
import time

class TencentSpider(object):
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

  # 获取工作职责和工作要求(发请求并解析二级页面)
  def get_job_duty(self,url):
    # 获取二级页面响应内容
    res = requests.get(url,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # xpath提取职责和要求
    parse_html = etree.HTML(html)
    jobobj_list = parse_html.xpath(
      '//tr[@class="c"]/td/ul[@class="squareli"]')
    # ['element ul at 地址','element ul at 地址']
    duty = '\n'.join(jobobj_list[0].xpath(
                              './/li/text()'))
    requirement = '\n'.join(jobobj_list[1].xpath(
                              './/li/text()'))
    return duty,requirement



  # 获取一级子界面职位信息
  def get_job_info(self,url,params):
    res = requests.get(url,params=params,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # 交给解析函数去做解析
    self.parse_job_info(html)

  # 解析职位信息
  def parse_job_info(self,html):
    # 创建解析对象
    parse_html = etree.HTML(html)
    # 基准xpath,匹配所有职位节点对象tr
    job_info_list = parse_html.xpath(
       '//tr[@class="even"] | //tr[@class="odd"]')
    # job_info_list:[tr对象1,tr对象2,...,tr对象10]
    for tr in job_info_list:
      job_link = 'https://hr.tencent.com/'+ \
                  tr.xpath('./td[1]/a/@href')[0]
      job_name = tr.xpath('./td[1]/a/text()')[0]
      job_type = tr.xpath('./td[2]/text()')[0]
      job_number = tr.xpath('./td[3]/text()')[0]
      job_address = tr.xpath('./td[4]/text()')[0]
      job_time = tr.xpath('./td[5]/text()')[0]
      job_duty,job_requirement = self.get_job_duty(job_link)


      d = {
        '职位链接:' : job_link,
        '职位名称:' : job_name,
        '职位类别:' : job_type,
        '招聘人数:' : job_number,
        '招聘地点:' : job_address,
        '发布时间:' : job_time,
        '工作职责:' : job_duty,
        '工作要求:' : job_requirement
      }
      print(d)
      print('*' * 30)

  # 数据处理
  def write_page(self):
    pass

  # 主函数
  def work_on(self):
    job = input('请输入职位方向:')

    for pn in range(0,2001,10):
      url = 'https://hr.tencent.com/position.php?'
      params = {
          'keywords': job,
          'start' : str(pn)
        }
      self.get_job_info(url,params)
      time.sleep(2)


if __name__ == '__main__':
  start = time.time()
  spider = TencentSpider()
  spider.work_on()
  end = time.time()
  print('执行时间:%.2f' % (end-start))










