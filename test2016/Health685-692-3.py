from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [685, 692, 693, 964]
Travel = webdriver.Chrome()
for i in mond:
    Travel.get("http://test2016.4008822300.net.cn/Health/Product/HospitalProductT%s-0-18-0.html" % i)
    time.sleep(2)
    Travel.find_element_by_id('ibtnBuy2').click()
    Travel.implicitly_wait(400)
    time.sleep(2)
    Travel.find_element_by_class_name('lg_close').click()
    Travel.find_element_by_id('txtSubStart').send_keys(d2)
    Travel.find_element_by_id('txtSName').send_keys('测试占志才')
    sltSType = Travel.find_element_by_id('sltSType')
    Select(sltSType).select_by_value('0')
    Travel.find_element_by_id('txtSNo').send_keys('432503197505028819')
    Travel.find_element_by_id('txtSPhone').send_keys('13243733102')
    Travel.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
    Travel.find_element_by_id('rdoMe').click()
    Travel.find_element_by_id('btnpostdate').click()
    Travel.implicitly_wait(4000)
    Travel.find_element_by_id('agree').click()
    Travel.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[12]/img[2]").click()
    time.sleep(2)
    texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    print("DI = " + str(i) + " 订单号：" + texts.text)
    Travel.implicitly_wait(4000)
Travel.quit()
