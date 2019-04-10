from selenium import webdriver

#
driver = webdriver.PhantomJS()
url = "https://www.qiushibaike.com/text/"
driver.get(url)
ele = driver.find_elements_by_class_name('content')
for r in ele:
    print(r.text)
    print("*"*50)

driver.close()
driver.quit()