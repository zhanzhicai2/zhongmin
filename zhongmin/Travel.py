from selenium import webdriver
import time,datetime
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 时间+30
d1 = datetime.datetime.now()
d3 = datetime.date(d1.year,d1.month+1,d1.day)
d2 = d3.strftime('%Y-%m-%d')
broweb = webdriver.Chrome()
def by_id(parameter_list):
    broweb.find_element_by_id(parameter_list).click()
broweb.get('http://test2016.4008822300.net.cn/Travel/TravelBuyNew2.aspx?id=896&day=2')
broweb.find_element_by_id('txtUserName').send_keys('13243733102')
broweb.find_element_by_xpath(".//*[@id='txtPassWord_text']").click()
broweb.find_element_by_id('txtPassWord').send_keys('zhan18702655166')
broweb.find_element_by_id('btnAllLogin').click()
time.sleep(3)
# broweb.find_element_by_class_name('lg_close').click()
broweb.find_element_by_id('txtSubStart').send_keys(d2)
broweb.implicitly_wait(3000)
# broweb.find_element_by_id('holdersub0').click()

ids = ['holdersub0','in1_6518474','btnpostdate','agree','imgBuy']

for value in ids:
    by_id(value)
    time.sleep(2)

# broweb.find_element_by_id('in1_6518474').click()

# broweb.find_element_by_id('btnpostdate').click()
# broweb.find_element_by_id('agree').click()
# broweb.find_element_by_id('holdersub0').click()
# by_id('imgBuy')