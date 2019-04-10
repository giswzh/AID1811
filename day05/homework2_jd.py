from selenium import webdriver
import time
import csv
# 显性等待模块和类的导入
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS()
url = 'https://www.jd.com/'
page = 1

def get_page():
    driver.get(url)
    goodsName = input('请输入要查询的商品')
    driver.find_element_by_id('key').send_keys(goodsName)
    driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
    #等待加载
    wait = WebDriverWait(driver,10)
    wait.until(ec.presence_of_all_elements_located(By.CLASS_NAME,"gl-warp clearfix"))

def parse_page():
    # 执行脚本,进度条拉倒最下面
    driver.execute_script(
        'window.scrollTo(0,document.body.scrollHeight)'
    )
    wait = WebDriverWait(driver,10)
    wait.until(ec.presence_of_all_elements_located(By.CLASS_NAME,"gl-warp clearfix"))
    ele1 = driver.find_elements_by_xpath('//li[@class="gl-item"]')
    for i in ele1:
        print(i.text)
        print("*"*50)
def write_csv():
    with open('jd','w') as f:
        writer = csv.writer(f)
        writer.writerow()


# 执行
get_page()
while True:
    parse_page()
    print('第%d页爬取完成' %page)
    page += 1
    if driver.page_source.find_element_by_class_name("pn-next disable") == -1:
        print('翻过了一页')
        driver.find_element_by_class_name("pn-next").click()
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_all_elements_located(By.CLASS_NAME, "gl-warp clearfix"))
    else:
        break
    # price = ele1.text.find_elements_by_xpath('./div/div[2]/strong/i')




