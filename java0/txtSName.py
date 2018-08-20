import time
import collections
from selenium.webdriver.support.ui import Select

js = "var q=document.documentElement.scrollTop=10000"
# 银行
def bank(title):
    elect_id(title, [("sltBProvince", "19"), ("sltBCity", "440300"), ("selbank", "DEBITBOC")])
    title.find_element_by_id('txtbankcode').send_keys('6217582000025986613')
    title.find_element_by_id('txtbankcodesure').send_keys('6217582000025986613')


# 下拉框
def elect_id(title, kwargs):
    for id, keys in kwargs:
        id = title.find_element_by_id(id)
        Select(id).select_by_value(keys)
        title.implicitly_wait(2000)


# 基本投保人信息
def applicant_info(title, sheng):
    title.find_element_by_id('txtSName').send_keys('测试占志才u')
    sltSType = title.find_element_by_id('sltSType')
    Select(sltSType).select_by_value('0')
    title.find_element_by_id('txtSNo').send_keys(sheng)
    title.find_element_by_id('txtSPhone').send_keys('13246778556')
    title.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')

# 被投保人信息
def sorder_info(title):
    sltRel1 = title.find_element_by_id('sltRel1')
    Select(sltRel1).select_by_value('0')
    title.find_element_by_id('txtHName1').send_keys('测试占志才')
    sltHType1 = title.find_element_by_id('sltHType1')
    Select(sltHType1).select_by_value('0')
    title.find_element_by_id('txtSNo').send_keys("110101198001019939")
    title.find_element_by_id('txtHPhone1').send_keys('13246778516')


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


# 中意
def interfaces_minsheng(title):
    title.find_element_by_id('txtKeyCode').send_keys('minsheng2015')
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
    # 获取alert信息
    # 核保
    print("核保：" + underwriting + "承保：" + Approved)

