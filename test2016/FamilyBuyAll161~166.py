from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month+1, d1.day)
d2 = d3.strftime('%Y-%m-%d')
mond = [161, 162, 163, 164, 165, 166]
LiBuyNumberItem = {'LiBuyNumberItem0': '350982197103165971', 'LiBuyNumberItem1' : '411222197708257097', 'LiBuyNumberItem2': '511526198106104173', 'LiBuyNumberItem3': '533527198909210238', 'LiBuyNumberItem4': '150203199512020472'}
AccBuyAll = webdriver.Chrome()
for i in mond:
    for v, d in LiBuyNumberItem.items():
        AccBuyAll.get('http://test2016.4008822300.net.cn/family/Product/family%s.html' % i)
        time.sleep(2)
        AccBuyAll.find_element_by_id(v).click()
        AccBuyAll.find_element_by_id('spanBuy').click()
        AccBuyAll.implicitly_wait(4000)
        AccBuyAll.find_element_by_class_name('lg_close').click()
        AccBuyAll.implicitly_wait(2000)
        AccBuyAll.find_element_by_id('txtSubStart').send_keys(d2)
        AccBuyAll.find_element_by_id('txtSName').send_keys('测试占志才')
        sltSType = AccBuyAll.find_element_by_id('sltSType')
        Select(sltSType).select_by_value('0')
        AccBuyAll.find_element_by_id('txtSNo').send_keys(d)
        AccBuyAll.find_element_by_id('txtSPhone').send_keys('13243733102')
        AccBuyAll.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
        sltProvince = AccBuyAll.find_element_by_id('sltProvince')
        Select(sltProvince).select_by_value('19-440000')
        AccBuyAll.implicitly_wait(3000)
        sltCity = AccBuyAll.find_element_by_id('sltCity')
        Select(sltCity).select_by_value('233-440300')
        AccBuyAll.implicitly_wait(3000)
        AccBuyAll.find_element_by_id('txtAddress').send_keys('南山区白石洲塘头村五坊65号')
        AccBuyAll.find_element_by_id('rdoMe').click()
        sltHRel = AccBuyAll.find_element_by_id('sltHRel').find_elements_by_tag_name('option')
        sltHRel[1].click()
        AccBuyAll.implicitly_wait(3000)
        sltHProvince = AccBuyAll.find_element_by_id('sltHProvince')
        Select(sltHProvince).select_by_value('19-440000')
        AccBuyAll.implicitly_wait(3000)
        sltHCity = AccBuyAll.find_element_by_id('sltHCity')
        Select(sltHCity).select_by_value('233-440300')
        AccBuyAll.implicitly_wait(3000)
        AccBuyAll.find_element_by_id('txtHAddress').send_keys('南山区白石洲塘头村五坊65号')
        sltHouseType1 = AccBuyAll.find_element_by_id('sltHouseType1')
        Select(sltHouseType1).select_by_value('1')
        AccBuyAll.find_element_by_id('btnpostdate').click()
        AccBuyAll.implicitly_wait(2000)
        AccBuyAll.find_element_by_id('agree').click()
        AccBuyAll.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[17]/img[2]").click()
        AccBuyAll.implicitly_wait(3000)
        texts = AccBuyAll.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        OrderID = texts.text
        time.sleep(2)
        AccBuyAll.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
        time.sleep(2)
        AccBuyAll.find_element_by_id('txtSubnumber').send_keys(OrderID)
        AccBuyAll.find_element_by_id('txtKeyCode').send_keys('com2016')
        AccBuyAll.find_element_by_id('btnCheck').click()
        time.sleep(2)
        # 获取alert信息
        btnCheck = AccBuyAll.switch_to_alert()
        # 核保
        underwriting = btnCheck.text
        time.sleep(2)
        btnCheck.accept()
        AccBuyAll.find_element_by_id('btnCreate').click()
        time.sleep(2)
        # 获取alert信息
        btnCreate = AccBuyAll.switch_to_alert()
        # 承保
        Approved = btnCreate.text
        time.sleep(2)
        btnCreate.accept()
        AccBuyAll.find_element_by_id('btnCancel').click()
        time.sleep(2)
        BtnGetPolicy = AccBuyAll.switch_to_alert()
        # 获取保单
        BtnGetPolicy1 = BtnGetPolicy.text
        time.sleep(2)
        BtnGetPolicy.accept()
        AccBuyAll.find_element_by_id('BtnGetPolicy').click()
        time.sleep(2)
        # 获取alert信息
        btnCancel = AccBuyAll.switch_to_alert()
        # 撤保
        cancellation = btnCancel.text
        time.sleep(2)
        btnCancel.accept()
        time.sleep(2)
        print("DI = "+str(i)+" 订单号："+"  天数："+v+" "+OrderID+"核保：" + underwriting+"承保："+Approved+"撤保："+cancellation)
        print("获取保单：" + BtnGetPolicy1)
        AccBuyAll.implicitly_wait(4000)
AccBuyAll.quit()
