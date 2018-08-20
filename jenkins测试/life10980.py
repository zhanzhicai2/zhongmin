import random
import time
from selenium import webdriver

driver = webdriver.Chrome()
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()

listtxtSNo = ['110101197801010081|13200001931', '110101197609010049|13200013432', '110101198303010120|13200001343', '11010119880301008X|13200003254', '110101199503140135|13200002265', '110101199803140102|13200001376']


def job(buyPage, r0_JobOne1):
    driver.find_element_by_xpath(buyPage).click()
    driver.find_element_by_xpath(r0_JobOne1).click()

for i in range(1, len(listtxtSNo)+1):
    driver.get('https://test2018.zhongmin.cn/life/detail/ip10980_is1.html')
    driver.find_element_by_xpath('//*[@id="payTime"]/span[%s]' % i).click()
    driver.find_element_by_class_name('nums-input').clear()
    # driver.find_element_by_class_name('nums-input').send_keys(20*(random.randint(1, 7)))

    driver.implicitly_wait(3000)
    driver.find_element_by_class_name('purchase-btn').click()
    time.sleep(2)
    driver.find_element_by_class_name('continue-btn').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[1]/dl[1]/dd/div/span').click()
    driver.find_element_by_xpath('//*[@id="iReal1"]/li[1]').click()
    driver.find_element_by_id('txtSName').send_keys('王曹')
    driver.find_element_by_id('identityType').click()
    driver.find_element_by_xpath('//*[@id="sltSType"]/li[2]').click()
    listtxtSNos = listtxtSNo[i - 1].split('|')
    driver.find_element_by_id('txtSNo').send_keys(listtxtSNos[0])
    print(listtxtSNos[0])
    print(listtxtSNos[1])
    driver.find_element_by_id('txtSPhone').send_keys(listtxtSNos[1])
    driver.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
    driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[2]/dl[9]/dd').click()
    driver.find_element_by_id('longEffective').click()
    driver.find_element_by_id('sltProvinceSpan').click()
    driver.find_element_by_xpath('//*[@id="sltProvince"]/li[13]').click()
    driver.find_element_by_id('sltCitySpan').click()
    driver.find_element_by_xpath('//*[@id="sltCity"]/li[3]').click()
    driver.find_element_by_id('stxtAddress').send_keys('金融科技大厦12楼')
    driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[5]/div/dl[15]/dd/div/span').click()
    time.sleep(1)
    r0_BuyNumber1 = 1
    driver.implicitly_wait(6000)
    driver.find_element_by_xpath('//*[@id="r0_BuyNumber1"]/li[%s]' % r0_BuyNumber1).click()
    print(r0_BuyNumber1)
    driver.implicitly_wait(6000)
    driver.implicitly_wait(3000)
    job('//*[@id="buyPage"]/div[1]/div[5]/div/dl[29]/dd/div[1]/span', '//*[@id="r0_JobOne1"]/li[1]')
    driver.implicitly_wait(3000)
    time.sleep(2)
    job('//*[@id="buyPage"]/div[1]/div[5]/div/dl[29]/dd/div[2]/span', '//*[@id="r0_JobTwo1"]/li')
    driver.implicitly_wait(3000)
    time.sleep(2)
    job('//*[@id="buyPage"]/div[1]/div[5]/div/dl[29]/dd/div[3]/span', '//*[@id="r0_JobThere1"]/li[1]')
    driver.implicitly_wait(3000)
    if i != 1:
        job('//*[@id="buyPage"]/div[1]/div[6]/dl[1]/dd/div[1]/span', '//*[@id="bankProvince"]/li[19]')
        driver.implicitly_wait(2000)
        job('//*[@id="buyPage"]/div[1]/div[6]/dl[1]/dd/div[2]/span', '//*[@id="bankCity"]/li[3]')
        driver.implicitly_wait(4000)
        job('//*[@id="buyPage"]/div[1]/div[6]/dl[2]/dd/div/span','//*[@id="bankName"]/li[2]')
        driver.implicitly_wait(2000)
        bankCode = '12365487955424754'+str(i)
        driver.find_element_by_id('bankCode').send_keys(bankCode)
        driver.find_element_by_id('confirmBankCode').send_keys(bankCode)
    driver.find_element_by_id('termsOfInform').click()
    driver.find_element_by_id('btnpostdate1').click()
    time.sleep(3)
# driver.quit()



