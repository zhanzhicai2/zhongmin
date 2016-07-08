import io
import sys
import time#时间
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# from selenium import webdriver
import unittest,time
from selenium.webdriver.support.ui import Select

def login(self):
    driver = self.driver
    driver.find_element_by_id('spanBuy').click()
    driver.find_element_by_class_name('lg_close').click()
    def GetNowTime():
        return time.strftime("%Y-%m-%d")
    driver.find_element_by_id("txtSubStart").send_keys(GetNowTime())
    driver.find_element_by_id('txtSName').send_keys("占志才")
    sel = driver.find_element_by_xpath("//select[@id='sltSType']")
    Select(sel).select_by_value('0')
    driver.find_element_by_id('txtSNo').send_keys("440301198306014861")
    driver.implicitly_wait(30000)
    driver.find_element_by_id('txtSPhone').send_keys('13243733102')
    driver.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')