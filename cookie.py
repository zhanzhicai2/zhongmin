# from selenium import webdriver
from selenium import webdriver
b = webdriver.Chrome()
b.git('http://www.baidu.com')
b.find_element_by_id('nih').find_element_by_id('take').click()
b.find_element_by_id('ddd').send_keys('nihgao')
