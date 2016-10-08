from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime
import txtSName

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [905]
# , 904, 905,902  'LiDayItem3', 'LiDayItem7', 'LiDayItem15', 'LiDayItem30', 'LiDayItem90', LiDayItem1', 'LiDayItem2','LiDayItem3', 'LiDayItem7', 'LiDayItem15', 'LiDayItem365',
LiDayItem = ['LiDayItem3', 'LiDayItem7', 'LiDayItem15', 'LiDayItem30', 'LiDayItem90', 'LiDayItem365']
Travel = webdriver.Chrome()
for i in mond:
    # Travel = webdriver.Chrome()
    # Travel.find_element_by_xpath(".//*[@id='LiDayItem365']").click()
    for d in LiDayItem:
        Travel.get("http://test2016.4008822300.net.cn/Travel/Product/travel%s.html" % i)
        time.sleep(2)
        Travel.find_element_by_id(d).click()
        Travel.implicitly_wait(400)
        Travel.find_element_by_id('ibtnBuy').click()
        time.sleep(2)
        Travel.find_element_by_class_name('lg_close').click()
        Travel.find_element_by_id('txtSubStart').send_keys(d2)
        Travel.find_element_by_id('txtSName').send_keys('测试占志才')
        sltSType = Travel.find_element_by_id('sltSType')
        Select(sltSType).select_by_value('0')
        Travel.find_element_by_id('txtSNo').send_keys('330224196702265835')
        Travel.find_element_by_id('txtSPhone').send_keys('13243733102')
        Travel.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
        Travel.find_element_by_id('rdoMe').click()
        Travel.find_element_by_id('btnpostdate').click()
        Travel.implicitly_wait(4000)
        Travel.find_element_by_id('agree').click()
        Travel.find_element_by_id('imgBuy').click()
        time.sleep(2)
        texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        OrderID = texts.text
        time.sleep(2)
        txtSName.interfaces(Travel, OrderID)
        # Travel.get("http://test2016.4008822300.net.cn/Interface_Test/ZhongYi.aspx")
        # time.sleep(2)
        # Travel.find_element_by_id('txtSubnumber').send_keys(OrderID)
        # Travel.find_element_by_id('txtKeyCode').send_keys('zhongyi2016')
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
        print("DI = "+str(i)+"  天数："+d+" 订单号："+OrderID+"核保："+underwriting+"承保："+Approved+"撤保："+cancellation)
        Travel.implicitly_wait(4000)
Travel.quit()




