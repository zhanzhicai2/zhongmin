import time
import unittest
from initial.frameworksd.browser_engine import BrowserEngine


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        try:
            assert '百度一下，你就知道' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
