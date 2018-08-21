from selenium import webdriver
driver = webdriver.Chrome()


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
    
    # 投保人信息
    def applicant_info(self, driver, info):
        driver.find_element_by_id('txtSubStart').send_keys(info.txtSubStart)
        driver.find_element_by_id('txtSName').send_keys(info.txtSName)
        identity_type(driver, info)
        driver.find_element_by_id('txtSPhone').send_keys(info.txtSPhone)
        driver.find_element_by_id('txtSEmail').send_keys(info.txtSEmail)

    # 投保人证件号区分
    def identity_type(self, driver, info):
        driver.find_element_by_id('identityType').click()
        slt_stype = info.sltSType
        slt_stype = '//*[@id="sltSType"]/li[' + slt_stype + ']'
        driver.find_element_by_xpath(slt_stype).click()
        driver.find_element_by_id('txtSNo').send_keys(info.txtSNo)
        # slt_stype  投保人证件号 0代表身份证
        if slt_stype != 0:
            driver.find_element_by_id('txtBirth').send_keys(info.txtBirth)
            sex = '//*[@id="sex"]/em[' + info.sex + ']'
            driver.find_element_by_xpath(sex).click()
        else:
            pass