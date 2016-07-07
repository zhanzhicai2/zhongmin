
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time
import dengru

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
        # driver.maximize_window()
        
        # #登录
        dengru.login(self)

        sele = brower.find_element_by_xpath("//select[@id='meJob1']")
        Select(sele).select_by_value('2202002-2')
        brower.find_element_by_id('btnpostdate').click()
        brower.find_element_by_id('agree').click()
        brower.find_element_by_id('imgBuy').click()

        # driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__userName']").clear()
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__userName']").send_keys('xxxx')
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__password']").clear()
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__password']").send_keys('xxxx')
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__submit']").click()
        # time.sleep(2)

        # #退出
        # div = driver.find_element_by_id('s_user_name_menu')
        # div.find_element_by_xpath(".//*[@id='s_user_name_menu']/div/a[5]/text()").click()
        # # div.find_element_by_class_name('quit').click()
        #
        # time.sleep(2)
        # driver.find_element_by_xpath(".//*[@id='tip_con_wrap']/div[3]/a[3]").click()
        # time.sleep(2)
        # print  '成功退出账户'


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

if __name__ == '__main__':
    unittest.main()