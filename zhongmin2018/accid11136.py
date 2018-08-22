from selenium import webdriver
import time
import io
import sys

broweb = webdriver.Chrome()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
for i in range(1, 5):
    broweb.get('https://www.zhongmin.cn/accid/detail/ip11136_is1.html')
    broweb.find_element_by_id('buy').click()
    broweb.find_element_by_xpath('//*[@id="clauseInfo"]/span/span/span/div[1]/a[1]').click()
    broweb.find_element_by_xpath('//*[@id="healthClause"]/div/div[2]/a').click()
    broweb.find_element_by_id('txtSubStart').send_keys('2018-08-24')
    broweb.find_element_by_id('txtSName').send_keys('低俗小说')
    broweb.find_element_by_id('identityType').click()
    time.sleep (3)
    broweb.find_element_by_xpath('//*[@id="sltSType"]/li[2]').click()
    broweb.find_element_by_id('txtSNo').send_keys('110101198005010130')
    broweb.find_element_by_id('txtSPhone').send_keys('13243733102')
    time.sleep (3)
    broweb.find_element_by_id('r0_Email1').send_keys('1610893869@qq.com')
    broweb.find_element_by_id ('txtSPhone').click()
    broweb.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[5]/div/dl[19]/dd/div/span').click()
    broweb.find_element_by_xpath('//*[@id="r0_BuyNumber1"]/li[1000]').click()
    time.sleep(10)
    broweb.find_element_by_id('termsOfInform').click()
    broweb.implicitly_wait(3000)
    broweb.find_element_by_id('btnpostdate1').click()
    time.sleep (10)