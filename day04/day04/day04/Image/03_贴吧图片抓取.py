import requests
from lxml import etree
import time

class BaiduImgSpider(object):
  def __init__(self):
    # 此处尽量使用IE的User-Agent,响应最标准
    self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    self.baseurl = 'http://tieba.baidu.com/f?'

  # 获取帖子链接函数
  def get_tlink(self,url,params):
    # 向贴吧发请求获取响应内容
    res = requests.get(url,params,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # xpath从响应内容中提取帖子链接
    parse_html = etree.HTML(html)
    tlink_list = parse_html.xpath('//div[@class="col2_right j_threadlist_li_right "]/div/div/a/@href')
    # tlink_list : ['/p/23232','/p/13543']
    for tlink in tlink_list:
      tlink = 'http://tieba.baidu.com' + tlink
      # get_imglink:提取1个帖子中图片链接保存本地
      self.get_imglink(tlink)

  # 获取图片链接函数
  def get_imglink(self,tlink):
    # 获取帖子响应内容
    res = requests.get(tlink,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.text
    # xpath提取图片链接列表
    parse_html = etree.HTML(html)
    # 图片 和 视频抓取
    # imglink_list = parse_html.xpath('//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video')
    # 视频
    imglink_list = parse_html.xpath(
'//div[@class="video_src_wrapper"]/embed/\
@data-video')
    # imglink_list : ['http://xxx.jpg','','']
    print(imglink_list)
    for imglink in imglink_list:
      self.write_img(imglink)

  # 保存图片
  def write_img(self,imglink):
    # 图片链接发请求获取响应内容
    res = requests.get(imglink,headers=self.headers)
    res.encoding = 'utf-8'
    html = res.content
    # 图片保存到本地
    filename = imglink[-10:]
    with open(filename,'wb') as f:
      f.write(html)
      print('%s-下载成功' % filename)

  # 主函数
  def work_on(self):
    name = input('请输入贴吧名:')
    start = int(input('请输入起始页:'))
    end = int(input('请输入终止页:'))
    for page in range(start,end+1):
      pn = (page-1)*50
      params = {
          'kw' : name,
          'pn' : str(pn)
      }
      # 调用函数一条龙
      self.get_tlink(self.baseurl,params)

if __name__ == '__main__':
  spider = BaiduImgSpider()
  spider.work_on()












