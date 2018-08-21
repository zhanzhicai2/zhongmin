from selenium import webdriver
from zhongminpython.zhongminpublic import ZhongMinPublic
import csv
import  time

driver = webdriver.Chrome()
zhongminpublic = ZhongMinPublic()
with open('accidexecl/accidexcel.csv') as accidexcel:
    driver.get(accidexcel.url)
    securityPeriod = driver.find_elements_by_xpath('//*[@id="securityPeriod"]/span')
    print(len(securityPeriod))
    if accidexcel.securityPeriod >= 0 & accidexcel.securityPeriod < len(securityPeriod):
        zhongminpublic.securityPeriod(driver, accidexcel.securityPeriod)
    else:
        print('securityPeriod 数字输入错误')
#     点击立即购买
    zhongminpublic.buy(driver)
#   txtSubStart 起保时间 0 代表 无需设置起保时间，页面是第二天起保。
    txtSubStart = accidexcel.txtSubStart
    if txtSubStart:
        if txtSubStart == 0:
            pass
        else:
            zhongminpublic.txtSubStart(driver, txtSubStart)







