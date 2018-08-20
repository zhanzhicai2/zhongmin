import random
import time
from selenium import webdriver
from jenkins测试.pubilcmian import bank, select_box, side_end

driver = webdriver.Chrome()
# option = webdriver.ChromeOptions()
# option.add_argument("headless")
# driver = webdriver.Chrome(chrome_options=option)
driver.maximize_window()

listtxtSNo = ['11010119800701010X|13200000311', '110101198507240032|13200000012', '110101198507240032|13200000013', '110101198707230074|13200000024', '110101199107240118|13200000015', '110101198703140098|13243733102', '110101197901010118|13200000017', '110101199501010097|13200000018', '110101199801010099|13200000019']
for i in range(6, 7):
    driver.get('https://test2018.zhongmin.cn/health/detail/is1_ip11096.html')
    driver.find_element_by_xpath('//*[@id="payTime"]/span[%s]' % i).click()
    driver.find_element_by_xpath('//*[@id="insured"]/span[%s]' % i).click()
    if i > 3 and i % 4 == 1:
        driver.find_element_by_xpath('//*[@id="group"]/div[1]/dl[1]/dd/span/span/span/span[2]').click()
    # elif i > 3 and i % 4 == 2:
        # driver.find_element_by_xpath('//*[@id="group"]/div[1]/dl[2]/dd/span/span/span/span[2]').click()
    elif i > 3 and i % 4 == 3:
        driver.find_element_by_xpath('//*[@id="group"]/div[1]/dl[1]/dd/span/span/span/span[2]').click()
        driver.find_element_by_xpath('//*[@id="group"]/div[1]/dl[2]/dd/span/span/span/span[2]').click()
    # driver.find_element_by_class_name('nums-input').send_keys(20*(random.randint(1, 7)))
    time.sleep(4)
    driver.find_element_by_class_name('purchase-btn').click()
    driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[1]/dl[1]/dd/div/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="iReal1"]/li[1]').click()
    driver.find_element_by_id('txtSName').send_keys('王曹')
    driver.find_element_by_id('identityType').click()
    driver.find_element_by_xpath('//*[@id="sltSType"]/li[2]').click()
    listtxtSNos = listtxtSNo[i - 1].split('|')
    driver.find_element_by_id('txtSNo').send_keys(listtxtSNos[0])
    driver.find_element_by_id('txtSPhone').send_keys(listtxtSNos[1])
    driver.find_element_by_id('txtSEmail').send_keys('1610893869@qq.com')
    driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[2]/dl[9]/dd').click()
    # 证件是否长期有效
    side_end(driver)
    # 地址
    select_box(driver, [('sltProvinceSpan','//*[@id="sltProvince"]/li[19]'), ('sltCitySpan',
'//*[@id="sltCity"]/li[12]'), ('sltxianSpan', '//*[@id="sltxian"]/li[4]')])
    driver.find_element_by_id('stxtAddress').send_keys('金融科技大厦12楼')
    select_box(driver, [('//*[@id="buyPage"]/div[1]/div[2]/dl[23]/dd/div[1]/span', '//*[@id="IJob1"]/li[1]'), ('//*[@id="buyPage"]/div[1]/div[2]/dl[23]/dd/div[2]/span', '//*[@id="IJob2"]/li[1]'), ('//*[@id="buyPage"]/div[1]/div[2]/dl[23]/dd/div[3]/span', '//*[@id="IJob3"]/li'), ('//*[@id="buyPage"]/div[1]/div[2]/dl[23]/dd/div[4]/span', '//*[@id="IJob4"]/li')])
    driver.implicitly_wait(3000)
    driver.find_element_by_id('r0_Height1').send_keys('168')
    driver.find_element_by_id('r0_Weight1').send_keys('65')
    bank(driver)
    time.sleep(4)
    driver.find_element_by_id('termsOfInform').click()
    driver.find_element_by_id('btnpostdate1').click()
    driver.implicitly_wait(10000)
# driver.quit()



