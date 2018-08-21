import time
import os
import configparser


class ZhongMinPublic(object):

    # 详情页的保障期限
    def securityPeriod(self, driver, securityPeriod):
        for i in range(1, securityPeriod):
            driver.find_elements_by_xpath('//*[@id="securityPeriod"]/span[%s]' % i)
    
    # 立即购买
    def buy(self, driver):
        driver.find_element_by_id('buy').click()
    
    # 起保时间
    def txtSubStart(self, driver, txtSubStart):
        driver.find_element_by_id('txtSubStart').send_keys(txtSubStart)

    # 投保人证件号区分
    def identity_type(self, driver, info):
        driver.find_element_by_id('identityType').click()
        slt_stype = info.sltSType
        slt_stype = '//*[@id="sltSType"]/li[' + slt_stype + ']'
        driver.find_element_by_xpath(slt_stype).click()
        driver.find_element_by_id('txtSNo').send_keys(info.txtSNo)
        driver.find_element_by_id('txtBirth').clear()
        driver.find_element_by_id('txtBirth').send_keys(info.txtBirth)
        sex = '//*[@id="sex"]/em[' + info.sex + ']'
        driver.find_element_by_xpath(sex).click()

    # 投保人信息
    def applicant_info(self, driver, info):
        driver.find_element_by_id('txtSName').send_keys(info.txtSName)
        self.identity_type(driver, info)
        driver.find_element_by_id('txtSPhone').send_keys(info.txtSPhone)
        driver.find_element_by_id('txtSEmail').send_keys(info.txtSEmail)

    # 点击 本人已了解并接受以下条款和告知 和 立即购买
    def TermsOfInform(self, driver):
        driver.find_element_by_id('termsOfInform').click()
        driver.find_element_by_id('btnpostdate1').click()

    # 被保人信息
    def identity_type_two(self, driver, info):
        time.sleep(2)
        driver.find_element_by_id('r1_ChineseName1').send_keys(info.r1_ChineseName1)
        # r1_IdentityType1  被保人证件号 2 代表身份证
        slt_stype = info.r1_IdentityType1
        slt_stype = '//*[@id="r1_IdentityType1"]/li[' + slt_stype + ']'
        # 清除在填写不用判断是否是身份证
        driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[6]/dd/div/span').click()
        driver.find_element_by_xpath(slt_stype).click()
        driver.find_element_by_id('r1_IdentityCode1').send_keys(info.r1_IdentityCode1)
        driver.find_element_by_id('r1_BirthDay1').clear()
        driver.find_element_by_id('r1_BirthDay1').send_keys(info.r1_BirthDay1)
        sex = '//*[@id="r1_Sex1"]/em[' + info.r1_Sex1 + ']'
        driver.find_element_by_xpath(sex).click()
        driver.find_element_by_id('r1_MobilePhone1').send_keys(info.r1_MobilePhone1)

    def conf_zhongmin(self):
        # 获取文件的当前路径（绝对路径）
        cur_path = os.path.abspath(os.path.dirname(__file__))
        # 获取zhongmin.ini的路径
        config_path = os.path.dirname(cur_path) + '\zhongmin.ini'
        conf = configparser.ConfigParser()
        conf.read(config_path)
        value = conf.get('baseconf', 'DNS')
        return value
