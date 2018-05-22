#coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
#driver.quit()
http://m.filmfly.cn/Hd/ccb49/a1?entrystr=8iEdyWMAtL2hN9Ofj8UIN5%2C7HisPppTl%2FtY774GWGUCEeRQHeF1j3OWU4qqQn3eu1pT4f4T9WLqR%0AmyB7w%2FXecSVJMF3exM6I