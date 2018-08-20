# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestSeleniumIde(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.zhongmin.cn/health/HealthBuyCommon.aspx?id=955&bid=12&age=0&sex=0&span=0&money=100000&payMethod=1.0000&payMethodrate=1.0000&price=25&bir=&Periods=0"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium_ide(self):
        driver = self.driver
        driver.get(self.base_url + "/health/HealthBuyCommon.aspx?id=955&bid=12&age=0&sex=0&span=0&money=100000&payMethod=1.0000&payMethodrate=1.0000&price=25&bir=&Periods=0")
        driver.find_element_by_id("txtSName").clear()
        driver.find_element_by_id("txtSName").send_keys(u"占志才")
        Select(driver.find_element_by_id("sltSType")).select_by_visible_text(u"身份证")
        driver.find_element_by_id("txtSNo").clear()
        driver.find_element_by_id("txtSNo").send_keys("360681199105022219")
        driver.find_element_by_id("txtSPhone").clear()
        driver.find_element_by_id("txtSPhone").send_keys("13243733102")
        driver.find_element_by_id("txtSEmail").clear()
        driver.find_element_by_id("txtSEmail").send_keys("zhanzhicai@zhongmin.net.cn")
        Select(driver.find_element_by_id("sltProvince")).select_by_visible_text(u"广东省")
        Select(driver.find_element_by_id("sltCity")).select_by_visible_text(u"深圳市")
        driver.find_element_by_id("txtAddress").clear()
        driver.find_element_by_id("txtAddress").send_keys(u"经融科技大厦19楼")
        Select(driver.find_element_by_id("sltRel1")).select_by_visible_text(u"父母")
        driver.find_element_by_id("txtHName1").clear()
        driver.find_element_by_id("txtHName1").send_keys(u"占录")
        Select(driver.find_element_by_id("sltHType1")).select_by_visible_text(u"身份证")
        driver.find_element_by_id("txtHNo1").clear()
        driver.find_element_by_id("txtHNo1").send_keys("110101201501010054")
        Select(driver.find_element_by_id("sltHType1")).select_by_visible_text(u"护照")
        Select(driver.find_element_by_id("sltHType1")).select_by_visible_text(u"身份证")
        driver.find_element_by_id("txtHPhone1").clear()
        driver.find_element_by_id("txtHPhone1").send_keys("13243733102")
        Select(driver.find_element_by_id("sltInsuredAmout")).select_by_visible_text("1000000")
        driver.find_element_by_id("btnpostdate1").click()
        driver.find_element_by_id("agree").click()
        driver.find_element_by_xpath("//img[contains(@src,'http://images.zhongmin.cn/images/preview_14.gif')]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
