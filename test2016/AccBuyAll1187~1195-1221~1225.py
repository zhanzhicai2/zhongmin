from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime


d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [1187, 1188, 1189, 1221,  1222, 1223]
AccBuyAll = webdriver.Chrome()
for i in mond:
    AccBuyAll.get('http://www.zhongmin.cn/accid/Product/accident%s.html' % i)
    AccBuyAll.find_element_by_id('spanBuy').click()
    time.sleep(2)
    AccBuyAll.find_element_by_class_name('lg_close').click()
    AccBuyAll.implicitly_wait(2000)
    AccBuyAll.find_element_by_id('txtSubStart').send_keys(d2)
    AccBuyAll.find_element_by_id('txtSName').send_keys('测试占志才')
    sltSType = AccBuyAll.find_element_by_id('sltSType')
    Select(sltSType).select_by_value('0')
    AccBuyAll.find_element_by_id('txtSNo').send_keys('330224196702265835')
    AccBuyAll.find_element_by_id('txtSPhone').send_keys('13243733102')
    AccBuyAll.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
    sltRel1 = AccBuyAll.find_element_by_id('sltRel1')
    Select(sltRel1).select_by_value('1')
    AccBuyAll.find_element_by_id('txtHName1').send_keys('测试占志零')
    sltHType1 = AccBuyAll.find_element_by_id('sltHType1')
    Select(sltHType1).select_by_value('0')
    AccBuyAll.find_element_by_id('txtHNo1').send_keys('110101201408013293')
    AccBuyAll.implicitly_wait(2000)
    AccBuyAll.find_element_by_id('txtHPhone1').send_keys('13243733102')
    hJob11 = AccBuyAll.find_element_by_id('hJob11')
    Select(hJob11).select_by_value('120102-1')
    AccBuyAll.find_element_by_id('btnpostdate').click()
    AccBuyAll.implicitly_wait(2000)
    AccBuyAll.find_element_by_id('agree').click()
    AccBuyAll.find_element_by_id('imgBuy').click()
    AccBuyAll.implicitly_wait(3000)
    texts = AccBuyAll.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    OrderID = texts.text
    time.sleep(2)
    # AccBuyAll.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
    # time.sleep(2)
    # AccBuyAll.find_element_by_id('txtSubnumber').send_keys(OrderID)
    # AccBuyAll.find_element_by_id('txtKeyCode').send_keys('com2016')
    # AccBuyAll.find_element_by_id('btnCheck').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCheck = AccBuyAll.switch_to_alert()
    # # 核保
    # underwriting = btnCheck.text
    # time.sleep(2)
    # btnCheck.accept()
    # AccBuyAll.find_element_by_id('btnCreate').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCreate = AccBuyAll.switch_to_alert()
    # # 承保
    # Approved = btnCreate.text
    # time.sleep(2)
    # btnCreate.accept()
    # AccBuyAll.find_element_by_id('btnCancel').click()
    # time.sleep(2)
    # BtnGetPolicy = AccBuyAll.switch_to_alert()
    # # 获取保单
    # BtnGetPolicy1 = BtnGetPolicy.text
    # time.sleep(2)
    # BtnGetPolicy.accept()
    # AccBuyAll.find_element_by_id('BtnGetPolicy').click()
    # time.sleep(2)
    # # 获取alert信息
    # btnCancel = AccBuyAll.switch_to_alert()
    # # 撤保
    # cancellation = btnCancel.text
    # time.sleep(2)
    # btnCancel.accept()
    # time.sleep(2)
    print("DI = " + str(i) + " 订单号：" + OrderID)
    # print("DI = " + str(i) + " 订单号：" + OrderID + "核保：" + underwriting + "承保：" + Approved + "撤保：" + cancellation)
    # print("获取保单：" + BtnGetPolicy1)
    AccBuyAll.implicitly_wait(4000)
AccBuyAll.quit()
