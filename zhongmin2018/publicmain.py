import time

from selenium.webdriver.support.ui import Select

# 投保人信息
def applicant_info(title, info):
    title.find_element_by_id('txtSubStart').send_keys(info.txtSubStart)
    title.find_element_by_id('txtSName').send_keys(info.txtSName)
    identity_type(title, info)
    title.find_element_by_id('txtSPhone').send_keys(info.txtSPhone)
    title.find_element_by_id('txtSEmail').send_keys(info.txtSEmail)


# 投保人证件号区分
def identity_type(title, info):
    title.find_element_by_id('identityType').click()
    slt_stype = info.sltSType
    slt_stype = '//*[@id="sltSType"]/li[' + slt_stype + ']'
    title.find_element_by_xpath(slt_stype).click()
    title.find_element_by_id('txtSNo').send_keys(info.txtSNo)
    # slt_stype  投保人证件号 0代表身份证
    if slt_stype != 0:
        title.find_element_by_id('txtBirth').send_keys(info.txtBirth)
        sex = '//*[@id="sex"]/em[' + info.sex + ']'
        title.find_element_by_xpath(sex).click()
    else:
        pass


# 被保人证件号区分
def identity_type_two(title, info):
    title.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[6]/dd/div/span').click
    # r1_IdentityType1  被保人证件号 0 代表身份证
    slt_stype = info.r1_IdentityType1
    slt_stype = '//*[@id="r1_IdentityType1"]/li[' + slt_stype + ']'
    title.find_element_by_xpath(slt_stype).click()
    title.find_element_by_id('r1_IdentityCode1').send_keys(info.r1_IdentityCode1)
    if slt_stype != 0:
        title.find_element_by_id ('r1_BirthDay1').send_keys(info.r1_BirthDay1)
        sex = '//*[@id="r1_Sex1"]/em[' + info.r1_Sex1 + ']'
        title.find_element_by_xpath(sex).click()


# 2层投保人地区 地区是北京
def applicant_area(title):
    title.find_element_by_id('sltProvinceSpan').click()
    slt_province = '//*[@id="sltProvince"]/li[1]'
    title.find_element_by_xpath(slt_province).click()
    title.find_element_by_id('sltCitySpan').click()
    title.find_element_by_xpath('//*[@id="sltCity"]/li').click()
    title.find_element_by_id('stxtAddress').send_keys('金融科技大厦12楼')


# 投保份数 默认一份
def lnsure_number(title):
    title.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[15]/dd/div/span').click()
    title.find_element_by_xpath('//*[@id="r1_BuyNumber1"]/li[1]').click()


# 下拉框
def elect_id(title, kwargs):
    for id, keys in kwargs:
        id = title.find_element_by_id(id)
        Select(id).select_by_value(keys)
        title.implicitly_wait(2000)
# 职业
# def applicant_job(title, info):


