from selenium import webdriver
from time import sleep

brower = webdriver.Chrome()
brower.get('https://login.zhongmin.cn/login.aspx')

brower.find_element_by_id('txtUserNameLogin').click()
brower.find_element_by_id('txtUserNameLogin').send_keys('13243733102')
brower.implicitly_wait(3000)
brower.find_element_by_id('txtShowPassWordLogin').click()
brower.find_element_by_id('txtShowPassWordLogin').send_keys('123456')
brower.find_element_by_id('btnUsualLogin').click()
