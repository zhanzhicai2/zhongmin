
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time
import tbrxx_tit

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url ='http://test2016.4008822300.net.cn/accid/Product/accident1161.html/'
        self.verficationErrors = []
        self.accept_next_alert =True
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #登录

        # #投保人信息
        tbrxx_tit.tbrxx_tit(self)

        sele = driver.find_element_by_xpath("//select[@id='meJob1']")
        Select(sele).select_by_value('2202002-2')
        driver.find_element_by_id('btnpostdate').click()
        # driver.find_element_by_id('agree').click()
        # driver.find_element_by_id('imgBuy').click()
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([],self.verficationErrors)
if __name__ == '__main__':
    unittest.main()