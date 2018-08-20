from selenium import webdriver
import time
import datetime
import io
import sys
from selenium.webdriver.support.ui import Select
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 时间+30
d1 = datetime.datetime.now()
d3 = datetime.date(d1.year,d1.month+1,d1.day)
d2 = d3.strftime('%Y-%m-%d')
broweb = webdriver.Chrome()
def by_id(parameter_list):
    broweb.find_element_by_id(parameter_list).click()
broweb.get('http://www.zhongmin.cn/Health/Product/HospitalProductT700-0-19-0.html')
broweb.find_element_by_id('ibtnBuy2').click()
broweb.implicitly_wait(30)
broweb.find_element_by_id('txtUserName').send_keys('13243733102')
broweb.find_element_by_xpath(".//*[@id='txtPassWord_text']").click()
broweb.find_element_by_id('txtPassWord').send_keys('zhan18702655166')
broweb.find_element_by_id('btnAllLogin').click()
time.sleep(3)
# 健康告知
broweb.find_element_by_id('healNo').find_element_by_class_name('mr16').click()
broweb.find_element_by_class_name('gz_next').click()
# broweb.find_element_by_class_name('lg_close').click()
# 时间
broweb.find_element_by_id('txtSubStart').send_keys(d2)
broweb.implicitly_wait(3000)
# broweb.find_element_by_id('holdersub0').click()
by_id('holdersub0')
# 地址 
loads1 = broweb.find_element_by_css_selector('#sltProvince')
Select(loads1).select_by_value('19-440000')
time.sleep(2)
loads2 = broweb.find_element_by_id('sltCity')
Select(loads2).select_by_value('233-440300')
time.sleep(2)
broweb.find_element_by_id('txtAddress').send_keys('南山区白石洲塘头村五坊65号')
broweb.find_element_by_id('txtPostCode').send_keys('554400')


# 投保人信息
def SelectZ(id, keys):
    selects = broweb.find_element_by_xpath(id)
    Select(selects).select_by_value(keys)
   
# 本人
sltRel1 = broweb.find_element_by_id('sltRel1')
Select(sltRel1).select_by_value('0')
time.sleep(2)
# 职业
job = [('hJob11', '2'), ('hJob21', '28'), ('hJob31', '0201001-1')]
SelectZ(".//*[@id='hJob11']", '2')
selects1 = broweb.find_element_by_xpath('hJob11').find_element_by_id('hJob21')
Select(selects1).select_by_value(28)
# for value,keys in job:
#     SelectZ(value,keys)
#     time.sleep(2)


ids = ['btnpostdate1','agree','imgBuy']

for value in ids:
    by_id(value)
    time.sleep(2)

