# 导入webdriver接口
from selenium import webdriver
import time
# 创建浏览器对象
driver = webdriver.PhantomJS()

# 向百度发起请求
driver.get('http://www.baidu.com/')
# 获取网页源码
print(driver.page_source)
print(driver.page_source.find("fjafdjoifnvzvopiewrwenr34"))
# 接受终端输入,发送到搜索框
key = input('请输入搜索内容')
kw = driver.find_element_by_id('kw')
kw.send_keys(key)
# 点击 百度一下 按钮
time.sleep(1)
su = driver.find_element_by_id('su')
su.click()

# 获取屏幕截图
driver.save_screenshot('zhaoliying.png')
# 关闭浏览器
driver.quit()