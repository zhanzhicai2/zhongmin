from selenium import webdriver
from txtSName import travel
import time
import datetime
import os

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [1268]
Travel = webdriver.Chrome()
# Travel = webdriver.Firefox()
for i in mond:
    Travel.get("http://www.zhongmin.cn/accid/Product/accident%s.html" % i)
    time.sleep(2)
    Travel.find_element_by_id('abuyurl1').click()
    Travel.implicitly_wait(400)
    time.sleep(2)
    travel(Travel, d2)
    texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    OrderID = texts.text
    time.sleep(2)
    # Travel.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
    # time.sleep(2)
    # Travel.find_element_by_id('txtSubnumber').send_keys(OrderID)
    # Travel.find_element_by_id('txtKeyCode').send_keys('com2016')
    # # texts2016 = {'btnCheck': 'underwriting', 'btnCreate': 'btnCreate', 'btnCancel': 'cancellation'}
    # Travel.find_element_by_id('btnCheck').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCheck = Travel.switch_to_alert()
    # # 核保
    # underwriting = btnCheck.text
    # time.sleep(2)
    # btnCheck.accept()
    # Travel.find_element_by_id('btnCreate').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCreate = Travel.switch_to_alert()
    # # 核保
    # Approved = btnCreate.text
    # time.sleep(2)
    # btnCreate.accept()
    # Travel.find_element_by_id('btnCancel').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCancel = Travel.switch_to_alert()
    # # 核保
    # cancellation = btnCancel.text
    # time.sleep(2)
    # btnCancel.accept()
    # time.sleep(2)
    print("DI = " + str(i) + " 订单号：" + OrderID)
    Travel.implicitly_wait(4000)
Travel.quit()

