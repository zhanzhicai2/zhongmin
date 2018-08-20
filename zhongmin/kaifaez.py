# from selenium import webdriver
# import time,datetime
# import io
# import sys


from selenium import webdriver
import time

ka_fa_web = webdriver.Chrome()
ka_fa_web.get('http://kaifa.ez-wms.com/')
ka_fa_web.find_element_by_id('userName').send_keys('yl')
ka_fa_web.find_element_by_id('userPass').send_keys('0000')
ka_fa_web.find_element_by_id('login').click()
ka_fa_web.implicitly_wait(20000)
ka_fa_web.find_element_by_class_name('li_hover').click()
ka_fa_web.implicitly_wait(10000)
ka_fa_web.find_element_by_xpath('//*[@id="column"]/div[2]/ul[1]/li/a').click()
ka_fa_web.find_element_by_link_text('新建订单').click()
ka_fa_web.implicitly_wait(20000)
ka_fa_web.find_element_by_class_name('headNav').click()
ka_fa_web.find_element_by_id('ship_warehouse').click()

ka_fa_web.implicitly_wait(10000)
ka_fa_web.find_element_by_xpath('//*[@id="ship_warehouse"]/option[1]').click()
