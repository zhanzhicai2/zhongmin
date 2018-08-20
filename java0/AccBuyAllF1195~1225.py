from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime


d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [7834]
AccBuyAll = webdriver.Chrome()
for i in mond:
    AccBuyAll.get('https://java01.zhongmin.cn/accid/detail/ip%s_is1' % i)

    AccBuyAll.find_element_by_class_name('purchase-btn').click()
    time.sleep(2)
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[1]/dl[1]/dd/div').click()
    AccBuyAll.implicitly_wait(3000)
    AccBuyAll.find_element_by_xpath('//*[@id="iReal1"]/li[1]').click()
    AccBuyAll.find_element_by_id('txtSubStart').send_keys('2018-03-30')
    # AccBuyAll.find_element_by_xpath('//*[@id="txtSubStart"]').send_keys('2018-03-30')
    AccBuyAll.find_element_by_id('txtSName').send_keys('测试占志才')
    AccBuyAll.find_element_by_id('identityType').click()
    AccBuyAll.find_element_by_xpath('//*[@id="sltSType"]/li[2]').click()
    AccBuyAll.find_element_by_id('txtSNo').send_keys('330224196702265835')
    AccBuyAll.find_element_by_id('txtBirth').send_keys('1991-03-30')
    AccBuyAll.find_element_by_xpath('//*[@id="sex"]/em[1]').click()
    AccBuyAll.find_element_by_id('txtSPhone').send_keys('13243733102')
    AccBuyAll.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
    职业
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[28]/dd/div[1]/span').click()
    AccBuyAll.find_element_by_xpath('//*[@id="r0_JobOne1"]/li[2]').click()
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[28]/dd/div[2]/span').click()
    AccBuyAll.find_element_by_xpath('//*[@id="r0_JobTwo1"]/li[1]').click()
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[28]/dd/div[3]/span').click()
    AccBuyAll.find_element_by_xpath('//*[@id="r0_JobThere1"]/li[1]').click()

    # 父母
    AccBuyAll.find_element_by_id('termsOfInform').click()
    AccBuyAll.find_element_by_id('btnpostdate1').click()
