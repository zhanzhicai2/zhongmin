from selenium import webdriver
from time import sleep

br = webdriver.Chrome()
br.get('http://baidu.com')
br.find_element_by_xpath("//*[@id='u1']/a[7]").click()
# 加上等待时间
br.implicitly_wait(300000)

br.find_element_by_id('TANGRAM__PSP_8__userName').click()
br.find_element_by_id('TANGRAM__PSP_8__userName').send_keys('zhanzhicai2')

br.find_element_by_id('TANGRAM__PSP_8__password').click()
br.find_element_by_id('TANGRAM__PSP_8__password').send_keys('Zzhan0502')
br.find_element_by_id('TANGRAM__PSP_8__submit').click()