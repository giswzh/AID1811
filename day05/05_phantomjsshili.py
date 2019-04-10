# 导入selenium的webdriver接口

from selenium import webdriver

# 先创建浏览器对象
driver = webdriver.PhantomJS()
# 浏览器对象向浏览器发请求
driver.get('http://www.baidu.com')
# 先获取屏幕截图
driver.save_screenshot('百度.png')
# 关闭浏览器
driver.quit()
