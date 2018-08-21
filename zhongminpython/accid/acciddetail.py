import csv
import time
from selenium import webdriver
from collections import namedtuple
from zhongminpython.zhongminpublic.applicant import ZhongMinPublic

driver = webdriver.Chrome()
driver.maximize_window()
zhongminpublic = ZhongMinPublic()
with open('./accidexcel/accidexcel.csv') as accidexcel:
    csv_accidexcel = csv.reader(accidexcel)
    accidexcel_header = next(csv_accidexcel)
    Row_zhongmin = namedtuple('Row', accidexcel_header)
    for row in csv_accidexcel:
        zhongmin_row = Row_zhongmin(*row)
        # 获取配置文件zhongmin.ini
        value = zhongminpublic.conf_zhongmin()
        url = value+zhongmin_row.url
        driver.get(url)
        securityPeriod = driver.find_elements_by_xpath('//*[@id="securityPeriod"]/span')
        if int(zhongmin_row.securityPeriod) >= 0 & int(zhongmin_row.securityPeriod) < len(securityPeriod):
            zhongminpublic.securityPeriod(driver, int(zhongmin_row.securityPeriod))
        else:
            print('securityPeriod 数字输入错误')
    #     点击立即购买
        zhongminpublic.buy(driver)
    #   txtSubStart 起保时间 0 代表 无需设置起保时间，页面是第二天起保。
        txtSubStart = zhongmin_row.txtSubStart
        if txtSubStart:
            if txtSubStart == 0:
                pass
            else:
                zhongminpublic.txtSubStart(driver, txtSubStart)
    #     投保人的信息
        zhongminpublic.applicant_info(driver, zhongmin_row)
    #   被保人信息 1 代表本人
        r1_Relation1 = zhongmin_row.r1_Relation1
        driver.find_element_by_id('txtSPhone').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[1]/dd/div/span').click()
        if r1_Relation1 == 1:
            driver.find_element_by_xpath('//*[@id="r1_Relation1"]/li[%s]' % r1_Relation1).click()
        else:
            driver.find_element_by_xpath('//*[@id="r1_Relation1"]/li[%s]' % r1_Relation1).click()
            time.sleep(2)
            zhongminpublic.identity_type_two(driver, zhongmin_row)
        # 点击 本人已了解并接受以下条款和告知 和 立即购买
        zhongminpublic.TermsOfInform(driver)

driver.quit()








