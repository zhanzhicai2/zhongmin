from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime


d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [685, 692, 693, 694]
dic = open("%spass.txt" % d2, "w")
AccBuyAll = webdriver.Chrome()
for i in mond:
    AccBuyAll.get('http://www.zhongmin.cn/Health/Product/HospitalProductT%s-0-32-0.html' % i)
    AccBuyAll.find_element_by_id('ibtnBuy2').click()
    time.sleep(2)
    AccBuyAll.find_element_by_class_name('lg_close').click()
    AccBuyAll.implicitly_wait(2000)
    AccBuyAll.find_element_by_id('txtSubStart').send_keys(d2)
    AccBuyAll.find_element_by_id('txtSName').send_keys('测试占志才')
    sltSType = AccBuyAll.find_element_by_id('sltSType')
    Select(sltSType).select_by_value('0')
    AccBuyAll.find_element_by_id('txtSNo').send_keys('110101193608072135')
    AccBuyAll.find_element_by_id('txtSPhone').send_keys('13243733102')
    AccBuyAll.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
    AccBuyAll.find_element_by_id('rdoMe').click()
    AccBuyAll.find_element_by_id('btnpostdate').click()
    AccBuyAll.implicitly_wait(2000)
    AccBuyAll.find_element_by_id('agree').click()
    AccBuyAll.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[12]/img[2]").click()
    AccBuyAll.implicitly_wait(3000)
    texts = AccBuyAll.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    OrderID = texts.text
    time.sleep(2)
    print("DI = " + str(i) + " 订单号：" + OrderID)
    # print("获取保单：" + BtnGetPolicy1)
    dic.write("DI = " + str(i) + " 订单号：" + OrderID+"\n")
    AccBuyAll.implicitly_wait(4000)
dic.close()
