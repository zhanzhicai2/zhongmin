import time
from selenium import webdriver


def select_box(driver, kwargs):
    for id, keys in kwargs:
        driver.implicitly_wait(2000)
        if '//' in id:
            driver.find_element_by_xpath(id).click()
        else:
            driver.find_element_by_id(id).click()
        driver.find_element_by_xpath(keys).click()


# 银行
def bank(driver):
    select_box(driver, [('//*[@id="buyPage"]/div[1]/div[6]/dl[1]/dd/div[1]/span', '//*[@id="bankProvince"]/li[19]'), ('//*[@id="buyPage"]/div[1]/div[6]/dl[1]/dd/div[2]/span', '//*[@id="bankCity"]/li[3]'), ('//*[@id="buyPage"]/div[1]/div[6]/dl[2]/dd/div/span', '//*[@id="bankName"]/li[2]')])
    driver.implicitly_wait(2000)
    driver.find_element_by_id('bankCode').send_keys('12365487955424754')
    driver.find_element_by_id('confirmBankCode').send_keys('12365487955424754')


# 证件是否长期有效
def side_end(driver):
    driver.find_element_by_id('validityPeriod').click()
    driver.find_element_by_id('txtSIdentityStart').send_keys('2008-4-25')
    driver.find_element_by_id('txtSIdentityEnd').send_keys('2028-4-25')



# def ad
#     driver.find_element_by_id('sltProvinceSpan').click()
#     driver.find_element_by_xpath('//*[@id="sltProvince"]/li[19]').click()
#     driver.find_element_by_id('sltCitySpan').click()
#     driver.find_element_by_xpath('//*[@id="sltCity"]/li[12]').click()
#     driver.find_element_by_id('sltxianSpan').click()
#     driver.find_element_by_xpath('//*[@id="sltxian"]/li[4]').click()