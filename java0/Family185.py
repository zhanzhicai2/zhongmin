from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

js = "var q=document.documentElement.scrollTop=10000"
d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
# txtPassWordLogin = "zm12345"
mond = [8140]
AccBuyAll = webdriver.Chrome()
# 登录00网
# AccBuyAll.get('https://java02.00.com.cn/login00.jsp?sid=107')
# AccBuyAll.find_element_by_id('txtUserNameLogin').send_keys('13243733102')
# # time.sleep(2)
# AccBuyAll.find_element_by_class_name('loginBox').click()
# AccBuyAll.find_element_by_id('txtPassWordLogin').click()
# AccBuyAll.find_element_by_id('txtPwd').send_keys(txtPassWordLogin)
# AccBuyAll.find_element_by_id('ImageButton2').click()
for i in mond:
    time.sleep(2)
    AccBuyAll.get('https://java02.zhongmin.cn/accid/detail/ip%s_is1_acSCPGPL' % i)
    time.sleep(2)
    AccBuyAll.find_element_by_class_name('purchase-btn').click()
    time.sleep(2)
    # 健康告知
    AccBuyAll.execute_script(js)
    time.sleep(2)
    AccBuyAll.find_element_by_xpath('//*[@id="clauseInfo"]/span/span/span/div[1]/a[1]').click()
    time.sleep (2)
    AccBuyAll.find_element_by_xpath('//*[@id="healthClause"]/div/div[2]/a').click()
    time.sleep(2)
    # AccBuyAll.find_element_by_xpath('//*[@id="iReal1"]/li').click()
    #关系
    # AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[1]/dl[1]/dd/div/span').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="iReal1"]/li').click()

    AccBuyAll.find_element_by_id('txtSubStart').send_keys('2018-05-12')
    # AccBuyAll.find_element_by_xpath('//*[@id="txtSubStart"]').send_keys('2018-03-30')
    AccBuyAll.find_element_by_id('txtSName').send_keys('占志才')
    AccBuyAll.find_element_by_id('identityType').click()
    AccBuyAll.find_element_by_xpath('//*[@id="sltSType"]/li[2]').click()
    AccBuyAll.find_element_by_id('txtSNo').send_keys('110101198506010075')
    # AccBuyAll.find_element_by_id('txtBirth').send_keys('1991-03-30')
    AccBuyAll.find_element_by_xpath('//*[@id="sex"]/em[1]').click()
    AccBuyAll.find_element_by_id('txtSPhone').send_keys('13243733102')
    AccBuyAll.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
    # AccBuyAll.find_element_by_id('sltProvinceSpan').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="sltProvince"]/li[1]').click()
    # AccBuyAll.find_element_by_id('sltCitySpan').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="sltCity"]/li').click()
    # AccBuyAll.find_element_by_id('stxtAddress').send_keys('wonanchangshangzhaozilong')
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[4]/div[1]/div/dl[1]/dd/div/span').click()
    #  子女
    # AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[5]/dd/div/span').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="r0_IdentityType1"]/li[2]').click()
    AccBuyAll.find_element_by_xpath('//*[@id="r1_ChineseName1"]').send_keys('占龙')
    AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[5]/dd/div/span').click()
    AccBuyAll.find_element_by_id('r0_IdentityCode1').send_keys('11010120150601007X')
    AccBuyAll.find_element_by_xpath('//*[@id="r0_IdentityType1"]/li[2]').click()
    AccBuyAll.find_element_by_id('r0_IdentityCode1').click()
    AccBuyAll.find_element_by_id('r0_MobilePhone1').send_keys('13243733102')
    #
    # # 职业
    # AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[26]/dd/div[1]/span').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="r0_JobOne1"]/li').click() 南区去金融科技大厦19楼
    # AccBuyAll.find_element_by_xpath('//*[@id="buyPage"]/div/div[5]/div/dl[26]/dd/div[2]/span').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="r0_JobTwo1"]/li').click()


    AccBuyAll.find_element_by_xpath('//*[@id="r1_Relation1"]/li[1]').click()
    # AccBuyAll.find_element_by_xpath('//*[@id="r2_Relation1"]/li[1]').click()
    # AccBuyAll.find_element_by_id('txtcarid').send_keys('粤B12345')
    AccBuyAll.find_element_by_id('termsOfInform').click()
    AccBuyAll.find_element_by_id('btnpostdate1').click()
