from selenium import webdriver


url = 'https://mail.qq.com'
# 创建浏览器对象
browser = webdriver.PhantomJS()
# 发请求
browser.get(url)
# 切换到子框架
login_frame = browser.find_element_by_id('login_frame')
browser.switch_to_frame(login_frame)
# 发送用户名和密码
browser.find_element_by_id('u').send_keys('4223835')
browser.find_element_by_id('p').send_keys('hanjiarong8000')
# 点击登录按钮
browser.find_element_by_id('login_button').click()
# 屏幕截图
browser.save_screenshot('success.png')