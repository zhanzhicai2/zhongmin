from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(5)
cookie = driver.get_cookies()
print(cookie)
driver.quit()
input.__getattribute__