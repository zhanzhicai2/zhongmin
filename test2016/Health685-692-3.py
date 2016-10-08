from selenium import webdriver
from selenium.webdriver.support.ui import Select
from txtSName import travel
import time
import datetime
import os


d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [685, 692, 693, 964]

Travel = webdriver.Chrome()
# Travel = webdriver.Firefox()
for i in mond:
    Travel.get("http://test2016.4008822300.net.cn/Health/Product/HospitalProductT%s-0-18-0.html" % i)
    time.sleep(2)
    Travel.find_element_by_id('ibtnBuy2').click()
    Travel.implicitly_wait(400)
    time.sleep(2)
    travel(Travel, d2)
    texts = Travel.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    print("DI = " + str(i) + " 订单号：" + texts.text)
    Travel.implicitly_wait(4000)
Travel.quit()
