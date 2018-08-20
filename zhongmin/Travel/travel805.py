from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import txtSName
import csv
from collections import namedtuple


Travel = webdriver.Chrome()
with open('Travelname.csv') as health:
    health_csv = csv.reader(health)
    headings = next(health_csv)
    Row = namedtuple('Row', headings)
    for r in health_csv:
        row = Row(*r)
        url = 'http://www.zhongmin.cn/Travel/TravelBuyNew2.aspx?id=%s&day=5'
        Travel.get(url % row.Pid)
        Travel.find_element_by_class_name('lg_close').click()
        Travel.execute_script(txtSName.js)
        time.sleep(2)
        Travel.find_element_by_id('txtSubStart').send_keys('2017-12-2')
        Travel.find_element_by_id('txtSName').send_keys('测试占志才')
        sltSType = Travel.find_element_by_id('sltSType')
        Select(sltSType).select_by_value('0')
        Travel.find_element_by_id('txtSNo').send_keys('110101199108120118')
        Travel.find_element_by_id('txtSPhone').send_keys('13243733102')
        Travel.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
        # 本人 rdoMe 其他被保人rdoOther
        Travel.find_element_by_id('rdoOther').click()
        # 其他被保人
        sltRel1 = Travel.find_element_by_id('sltRel1')
        Select(sltRel1).select_by_value(row.value)
        Travel.find_element_by_id('txtHName1').clear()
        # rdoOthename  被保人的姓名
        Travel.find_element_by_id('txtHName1').send_keys(row.rdoOthername)
        sltHType1 = Travel.find_element_by_id('sltHType1')
        # 0 身份证 1 护照
        Select(sltHType1).select_by_value('0')
        Travel.find_element_by_id('txtHNo1').clear()
        Travel.find_element_by_id('txtHNo1').send_keys(row.txtSNo)
        sltHType1Vaule = int(row.sltHType1Vaule)
        if sltHType1Vaule > 0:
            Select(sltHType1).select_by_value(row.sltHType1Vaule)
            Travel.execute_script(txtSName.js)
        time.sleep(2)
        Travel.find_element_by_id('wTable').click()
        Travel.find_element_by_id('txtHPhone1').send_keys('13243733102')
        Travel.execute_script(txtSName.js)
        Travel.find_element_by_id('btnpostdate').click()
        # Travel.find_element_by_xpath('html/body/form/div[4]/div[8]/div/img').click()
        Travel.implicitly_wait(4000)
        Travel.execute_script(txtSName.js)
        Travel.find_element_by_id('agree').click()
        Travel.find_element_by_id('imgBuy').click()
        # Travel.find_element_by_xpath('html/body/form/div[5]/div[3]/div[12]/img[2]').click()
        time.sleep(2)
        texts = Travel.find_element_by_xpath("html/body/form/div[4]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
        OrderID = texts.text
        time.sleep(2)
        print(OrderID)
        Travel.implicitly_wait(4000)
        with open('testhealth.csv', 'a+', newline='') as test1_csv:
            writer = csv.writer(test1_csv)
            writer.writerow(r + [OrderID])
    Travel.quit()
health.close()


