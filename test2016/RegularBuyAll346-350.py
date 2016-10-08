import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def electId(id, keys):
    id = RegularDetail.find_element_by_id(id)
    Select(id).select_by_value(keys)
    RegularDetail.implicitly_wait(2000)

RegularDetail = webdriver.Chrome()
get_url = [347]
sltInsuredAmout = ['500000.00']
for url_id in get_url:
    RegularDetail.get('http://test2016.4008822300.net.cn/Regular/RegularBuyAll.aspx?id=%s&bid=26&dlid=9&valueid=2&price=88.00&sex=0&bir=' % url_id)
    for money in sltInsuredAmout:
        # RegularDetail.find_element_by_id(money).click()
        # RegularDetail.find_element_by_id('ibtnBuy2').click()
        RegularDetail.implicitly_wait(4000)
        RegularDetail.find_element_by_class_name('lg_close').click()
        RegularDetail.implicitly_wait(2000)
        time.sleep(4)
        RegularDetail.find_element_by_class_name('mr16').click()
        RegularDetail.find_element_by_class_name('gz_next').click()
        RegularDetail.implicitly_wait(2000)
        RegularDetail.find_element_by_id('txtSName').send_keys('测试占志才')
        sltSType = RegularDetail.find_element_by_id('sltSType')
        Select(sltSType).select_by_value('0')
        RegularDetail.find_element_by_id('txtSNo').send_keys("110101198003019975")
        RegularDetail.find_element_by_id('txtSPhone').send_keys('13246733516')
        RegularDetail.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
        electId('sltProvince', '16-410000')
        electId('sltCity', '187-410200')
        RegularDetail.find_element_by_id('txtAddress').send_keys('科技园科苑路金融大厦19层')
        RegularDetail.find_element_by_id('rdoMe').click()
        electId('sltInsuredAmout', money)
        electId('sltPeriods', '12')
        sltBCity = RegularDetail.find_element_by_id('sltBProvince')
        Select(sltBCity).select_by_value('19')
        RegularDetail.implicitly_wait(3000)
        sltBCity = RegularDetail.find_element_by_id('sltBCity')
        Select(sltBCity).select_by_value('440300')
        RegularDetail.implicitly_wait(3000)
        selbank = RegularDetail.find_element_by_id('selbank')
        Select(selbank).select_by_value('DEBITCMBCHIAN')
        RegularDetail.implicitly_wait(3000)

        RegularDetail.find_element_by_id('txtbankcode').send_keys('6214836557050727')
        RegularDetail.find_element_by_id('txtbankcodesure').send_keys('6214836557050727')
        RegularDetail.find_element_by_id('btnpostdate1').click()
        RegularDetail.implicitly_wait(3000)
        RegularDetail.find_element_by_id('agree').click()
        RegularDetail.implicitly_wait(4000)
        RegularDetail.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[13]/img[2]").click()
        RegularDetail.implicitly_wait(4000)
        texts = RegularDetail.find_element_by_xpath(".//*[@id='form1']/div[8]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        OrderID = texts.text
        time.sleep(2)
        RegularDetail.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
        time.sleep(2)
        RegularDetail.find_element_by_id('txtSubnumber').send_keys(OrderID)
        RegularDetail.find_element_by_id('txtKeyCode').send_keys('com2016')
        # texts2016 = {'btnCheck': 'underwriting', 'btnCreate': 'btnCreate', 'btnCancel': 'cancellation'}
        RegularDetail.find_element_by_id('btnCheck').click()
        time.sleep(2)
        # 获取alert信息
        btnCheck = RegularDetail.switch_to_alert()
        # 核保
        underwriting = btnCheck.text
        time.sleep(2)
        btnCheck.accept()
        RegularDetail.find_element_by_id('btnCreate').click()
        time.sleep(2)
        # 获取alert信息
        btnCreate = RegularDetail.switch_to_alert()
        # 核保
        Approved = btnCreate.text
        time.sleep(2)
        btnCreate.accept()
        RegularDetail.find_element_by_id('btnCancel').click()
        time.sleep(2)
        # 获取alert信息
        btnCancel = RegularDetail.switch_to_alert()
        # 核保
        cancellation = btnCancel.text
        time.sleep(2)
        btnCancel.accept()
        time.sleep(2)
        print("DI = " + str(url_id) + '金额：'+str(money)+" 订单号：" + OrderID + "核保：" + underwriting + "承保：" + Approved + "撤保：" + cancellation)
        RegularDetail.implicitly_wait(4000)
        RegularDetail.get('http://test2016.4008822300.net.cn/Regular/RegularBuyAll.aspx?id=%s&bid=26&dlid=9&valueid=2&price=88.00&sex=0&bir=' % url_id)
RegularDetail.quit()


