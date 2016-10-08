from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# , 'LiPaySpanItem3', 'LiPaySpanItem4', 'LiPaySpanItem5' 'LiMoneyItem0', 'LiMoneyItem1', 'LiMoneyItem2', 'LiMoneyItem3', 'LiMoneyItem4',LiPaySpanItem2  'LiMoneyItem5'
AccidProductNew = webdriver.Chrome()
mond = [622]


def selectid(id, keys):
    id = AccidProductNew.find_element_by_id(id)
    Select(id).select_by_value(keys)

for i in mond:
    AccidProductNew.get('http://www.zhongmin.cn/health/product/AccidProduct.aspx?id=%s' % i)
    LiPaySpanItem = ['LiPaySpanItem5']
    LiMoneyItem = ['LiMoneyItem2']
    # txtSNo = {'110101198001010010': '18702655112', '110101198001010053': '18702655112', '110101198001010096': '18702655118'}
    for PaySpan in LiPaySpanItem:
        AccidProductNew.find_element_by_id(PaySpan).click()
        for Money in LiMoneyItem:
            AccidProductNew.find_element_by_id(Money).click()
            time.sleep(2)
            LiHoldRemittedItems = AccidProductNew.find_elements_by_xpath(".//*[@id='UlHoldRemittedBelongs']/ul/li")
            for HoldRemitted, Items in enumerate(LiHoldRemittedItems):
                AccidProductNew.find_element_by_id('LiHoldRemittedItem%s' % HoldRemitted).click()
                print('LiHoldRemittedItem%s' % HoldRemitted)
                time.sleep(4)
                AccidProductNew.find_element_by_id('ibtnBuy2').click()
                AccidProductNew.implicitly_wait(4000)
                AccidProductNew.find_element_by_class_name('lg_close').click()
                AccidProductNew.implicitly_wait(2000)
                time.sleep(4)
                AccidProductNew.find_element_by_class_name('mr16').click()
                AccidProductNew.find_element_by_class_name('gz_next').click()
                AccidProductNew.implicitly_wait(2000)
                AccidProductNew.find_element_by_id('txtSName').send_keys('占志才')
                sltSType = AccidProductNew.find_element_by_id('sltSType')
                Select(sltSType).select_by_value('0')
                AccidProductNew.find_element_by_id('txtSNo').send_keys("110101198008180055")
                AccidProductNew.find_element_by_id('txtSPhone').send_keys('13243978986')
                AccidProductNew.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
                sltProvince = AccidProductNew.find_element_by_id('sltProvince')
                Select(sltProvince).select_by_value('19-440000')
                AccidProductNew.implicitly_wait(3000)
                sltCity = AccidProductNew.find_element_by_id('sltCity')
                Select(sltCity).select_by_value('246-440300')
                AccidProductNew.implicitly_wait(3000)
                selectid('sltxian', '2336-440305')
                # sltxian = AccidProductNew.find_element_by_id('sltxian')
                # Select(sltxian).select_by_value('2336-440305')
                AccidProductNew.implicitly_wait(3000)
                AccidProductNew.find_element_by_id('txtAddress').send_keys('南山区白石洲塘头村五坊65号')
                AccidProductNew.find_element_by_id('rdoMe').click()
                AccidProductNew.find_element_by_id('txtPostCode').send_keys('554400')
                sltProvince = AccidProductNew.find_element_by_id('meJob1')
                Select(sltProvince).select_by_value('5')
                sltProvince = AccidProductNew.find_element_by_id('meJob2')
                Select(sltProvince).select_by_value('1020202-1')
                AccidProductNew.find_element_by_id('txtMeHeight').send_keys('175')
                AccidProductNew.find_element_by_id('txtMeWeight').send_keys('60')
                sltBProvince = AccidProductNew.find_element_by_id('sltInsuredAmout')
                Select(sltBProvince).select_by_value('100000')
                AccidProductNew.implicitly_wait(3000)
                sltBCity = AccidProductNew.find_element_by_id('sltBProvince')
                Select(sltBCity).select_by_value('19')
                AccidProductNew.implicitly_wait(3000)
                sltBCity = AccidProductNew.find_element_by_id('sltBCity')
                Select(sltBCity).select_by_value('440300')
                AccidProductNew.implicitly_wait(3000)
                selbank = AccidProductNew.find_element_by_id('selbank')
                Select(selbank).select_by_value('DEBITCMBCHIAN')
                AccidProductNew.implicitly_wait(3000)

                AccidProductNew.find_element_by_id('txtbankcode').send_keys('6214836557050727')
                AccidProductNew.find_element_by_id('txtbankcodesure').send_keys('6214836557050727')
                AccidProductNew.find_element_by_id('btnpostdate1').click()
                AccidProductNew.implicitly_wait(3000)
                # AccidProductNew.find_element_by_id('agree').click()
                AccidProductNew.implicitly_wait(4000)
                AccidProductNew.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[13]/img[2]").click()
                # texts = AccidProductNew.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
                # OrderID = texts.text
                # time.sleep(2)
                # AccidProductNew.get("http://test2016.4008822300.net.cn/testpiccc.aspx")
                # time.sleep(2)
                # AccidProductNew.find_element_by_id('TextBox1').send_keys(OrderID)
                # # texts2016 = {'btnCheck': 'underwriting', 'btnCreate': 'btnCreate', 'btnCancel': 'cancellation'}
                # AccidProductNew.find_element_by_id('Button1').click()
                # time.sleep(2)
                # Button1 = AccidProductNew.find_element_by_xpath("html/body").text
                # AccidProductNew.find_element_by_id('Button3').click()
                # time.sleep(2)
                # Button3 = AccidProductNew.find_element_by_xpath("html/body").text
                # time.sleep(2)
                # print("ID"+str(i)+"年限："+str(span)+"保额："+str(MoneyItem)+" 订单号：" + OrderID + "核保：" + Button1 + "撤保：" + Button3)
                # print("ID"+str(i)+"年限："+str(span)+"保额："+str(MoneyItem)+" 订单号：" + OrderID)
                AccidProductNew.implicitly_wait(4000)
                # AccidProductNew.get('http://www.zhongmin.cn/health/product/AccidProduct.aspx?id=%s' % i)
                AccidProductNew.find_element_by_id(PaySpan).click()
                AccidProductNew.find_element_by_id(Money).click()
                time.sleep(2)
AccidProductNew.quit()




