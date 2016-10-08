from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

# 'LiDayItem7', 'LiDayItem10','LiDayItem14': '11010119800101015X',

Travel = webdriver.Chrome()
d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [893]
LiDayItem = {'LiDayItem7':'110101198001290016','LiDayItem14': '110101198001290059','LiDayItem17':'110101198001290075', 'LiDayItem21':'110101198001290139', 'LiDayItem30':'110101198001290219', 'LiDayItem60':'110101198001290251', 'LiDayItem90':'110101198001290278', 'LiDayItem365':'110101198001010555'}
for i in mond:
    Travel.get('http://test2016.4008822300.net.cn/Travel/Product/travel%s-18d1.html' % i)
    for Day, v in LiDayItem.items():
        Travel.find_element_by_id('ibtnBuy').click()
        Travel.implicitly_wait(4000)
        Travel.find_element_by_class_name('lg_close').click()
        Travel.find_element_by_id('txtSubStart').send_keys(d2)
        Travel.find_element_by_id('txtSName').send_keys('测试占志才')
        sltSType = Travel.find_element_by_id('sltSType')
        Select(sltSType).select_by_value('0')
        Travel.find_element_by_id('txtSNo').send_keys(v)
        Travel.find_element_by_id('txtSPhone').send_keys('13273533102')
        Travel.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
        Travel.find_element_by_id('rdoMe').click()
        Travel.find_element_by_id('btnpostdate').click()
        Travel.implicitly_wait(4000)
        Travel.find_element_by_id('agree').click()
        # Travel.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[12]/img[2]").click()
        Travel.find_element_by_id('imgBuy').click()
        texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        OrderID = texts.text
        time.sleep(2)
        Travel.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
        time.sleep(2)
        Travel.find_element_by_id('txtSubnumber').send_keys(OrderID)
        Travel.find_element_by_id('txtKeyCode').send_keys('com2016')
        # texts2016 = {'btnCheck': 'underwriting', 'btnCreate': 'btnCreate', 'btnCancel': 'cancellation'}
        Travel.find_element_by_id('btnCreate').click()
        time.sleep(2)
        # 获取alert信息
        btnCreate = Travel.switch_to_alert()
        # 承保
        Approved = btnCreate.text
        time.sleep(2)
        btnCreate.accept()
        Travel.find_element_by_id('btnCancel').click()
        time.sleep(2)
        # 获取alert信息
        btnCancel = Travel.switch_to_alert()
        # 撤保
        cancellation = btnCancel.text
        time.sleep(2)
        btnCancel.accept()
        time.sleep(2)
        print("DI = " + str(i) + "  天数：" + Day + " 订单号：" + OrderID + "承保：" + Approved + "撤保：" + cancellation)
        Travel.implicitly_wait(4000)
        Travel.get('http://test2016.4008822300.net.cn/Travel/Product/travel%s-18d1.html' % i)
Travel.quit()




