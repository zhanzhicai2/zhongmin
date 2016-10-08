from selenium.webdriver.support.ui import Select
import time


# 银行
def bank(title):
    elect_id(title, "sltBProvince", "19")
    elect_id(title, "sltBCity", "440300")
    elect_id(title, "selbank", "DEBITCMBCHIAN")
    title.find_element_by_id('txtbankcode').send_keys('6214836557050727')
    title.find_element_by_id('txtbankcodesure').send_keys('6214836557050727')


# 下拉框
def elect_id(title, id, keys):
    id = title.find_element_by_id(id)
    Select(id).select_by_value(keys)
    title.implicitly_wait(2000)


# 基本投保人信息
def applicant_info(title):
    title.find_element_by_id('txtSName').send_keys('测试占志才')
    sltSType = title.find_element_by_id('sltSType')
    Select(sltSType).select_by_value('0')
    title.find_element_by_id('txtSNo').send_keys("110101198001019939")
    title.find_element_by_id('txtSPhone').send_keys('13246778516')
    title.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')


def interfaces(title):
    title.find_element_by_id('txtKeyCode').send_keys('com2016')
    # texts2016 = {'btnCheck': 'underwriting', 'btnCreate': 'btnCreate', 'btnCancel': 'cancellation'}
    title.find_element_by_id('btnCheck').click()
    time.sleep(2)
    # 获取alert信息
    btnCheck = title.switch_to_alert()
    # 核保
    underwriting = btnCheck.text
    time.sleep(2)
    btnCheck.accept()
    title.find_element_by_id('btnCreate').click()
    time.sleep(2)
    # 获取alert信息
    btnCreate = title.switch_to_alert()
    # 核保
    Approved = btnCreate.text
    time.sleep(2)
    btnCreate.accept()
    title.find_element_by_id('btnCancel').click()
    time.sleep(2)
    # 获取alert信息
    btnCancel = title.switch_to_alert()
    # 核保
    cancellation = btnCancel.text
    time.sleep(2)
    btnCancel.accept()
    time.sleep(2)
    print("核保：" + underwriting + "承保：" + Approved + "撤保：" + cancellation)

