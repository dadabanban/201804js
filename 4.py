# coding=utf-8
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

first_url='http://www.baidu.com'
print("1%s" %(first_url))
driver.get(first_url)

s_url='http://news.baidu.com'
print("2%s" %(s_url))
driver.get(s_url)

print("back to %s" %(first_url))
driver.back()

print("forwar to %s" %(s_url))
driver.forward()

driver.refresh()
driver.refresh()
driver.refresh()
driver.refresh()





print("设置浏览器")
driver.set_window_size(480,800)
