from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [902, 903, 904, 905]
LiDayItem = ['LiDayItem1', 'LiDayItem2', 'LiDayItem3', 'LiDayItem7', 'LiDayItem15', 'LiDayItem30', 'LiDayItem365']
for i in mond:
    Travel = webdriver.Chrome()
    Travel.get("http://test2016.4008822300.net.cn/Travel/Product/travel%s.html" % i)
    # Travel.find_element_by_xpath(".//*[@id='LiDayItem365']").click()

    for d in LiDayItem:
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
        Travel.find_element_by_id('txtSNo').send_keys('450201197801275091')
        Travel.find_element_by_id('txtSPhone').send_keys('13243733102')
        Travel.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
        Travel.find_element_by_id('rdoMe').click()
        Travel.find_element_by_id('btnpostdate').click()
        Travel.implicitly_wait(4000)
        Travel.find_element_by_id('agree').click()
        Travel.find_element_by_id('imgBuy').click()
        Travel.implicitly_wait(4000)
        texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        print("DI = "+str(i)+"  天数："+d+" 订单号："+texts.text)
        Travel.implicitly_wait(4000)
        Travel.quit()




