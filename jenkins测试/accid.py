
import datetime
import time
from selenium import webdriver

NOW_TIME = datetime.datetime.now()+datetime.timedelta(days=8)
NOW_TIME = NOW_TIME.strftime('%Y-%m-%d')

driver = webdriver.Chrome()
driver.maximize_window()

# def accid():
for i in range(1, 7):
    driver.get('https://www.zhongmin.cn/travel/detail/ip11180_is1.html')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="policyTerm"]/span[%s]' % i).click()
    time.sleep(1)
    driver.find_element_by_class_name('purchase-btn').click()
    driver.find_element_by_xpath ('//*[@id="buyPage"]/div[1]/div[1]/dl[1]/dd/div/span').click()
    driver.find_element_by_xpath ('//*[@id="iReal1"]/li[1]').click()
    driver.find_element_by_id('txtSubStart').send_keys(NOW_TIME)
    driver.find_element_by_id('txtSName').send_keys('王曹')
    driver.find_element_by_id('identityType').click()
    driver.find_element_by_xpath('//*[@id="sltSType"]/li[3]').click()
    txtSNo = 'G010449%s' % i
    driver.find_element_by_id('txtSNo').send_keys(txtSNo)
    driver.find_element_by_id('txtBirth').send_keys('1991-11-14')
    driver.find_element_by_xpath('//*[@id="sex"]/em[2]').click()
    driver.find_element_by_id('txtSPhone').send_keys('13243733102')
    driver.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
    # driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[2]/dl[9]/dd').click()
    # driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[1]/dd/div/span').click()
    # driver.find_element_by_xpath('//*[@id="r1_Relation1"]/li[1]').click()
    driver.find_element_by_id('termsOfInform').click()
    driver.find_element_by_id('btnpostdate1').click()
    driver.implicitly_wait(4000)
    pay_info = driver.find_element_by_xpath('//*[@id="orderInfo"]/tbody/tr/td[1]/div/p').text
    # count_price = driver.find_element_by_class_name('count-price')
    # count_price = count_price.text
    # try:
    #     assert count_price in '1.00'
    #     print("价格没有问题哦")
    # except Exception as e:
    #     print('订单价格有问题')
    print(pay_info)
driver.quit()


# if __name__ == '__main__':
# accid()
