import io
import sys
import time#时间
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# from selenium import webdriver
from selenium.webdriver.support.ui import Select

def logo(self):
    print("sss")
    brower = self.brower
    brower.find_element_by_id('spanBuy').click()
    brower.find_element_by_class_name('lg_close').click()
    def GetNowTime():
        return time.strftime("%Y-%m-%d")
    brower.find_element_by_id("txtSubStart").send_keys(GetNowTime())
    brower.find_element_by_id('txtSName').send_keys("占志才")
    sel = brower.find_element_by_xpath("//select[@id='sltSType']")
    Select(sel).select_by_value('0')
    brower.find_element_by_id('txtSNo').send_keys("440301198306014861")
    brower.implicitly_wait(30000)
    brower.find_element_by_id('txtSPhone').send_keys('13243733102')
    brower.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')