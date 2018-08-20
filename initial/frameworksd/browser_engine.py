import os.path
import configparser
from selenium import webdriver
from initial.frameworksd.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    """
    """
    # 找到驱动的相对路径
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        '''

        :param driver:
        :return:
        '''
        config = configparser.ConfigParser()   # 读取config 的值
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get('browserType', 'browserName')
        logger.info("You had select %s browser." % browser)
        url = config.get('testServer', 'URL')
        logger.info("The test server url is: %s" % url)

        if browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == 'Firefox':
            logger.info("Starting Firefox browser.")
            driver = webdriver.Firefox()

        elif browser == 'IE':
            pass
            # driver = webdriver.Ie(self.ie_driver_path)  目前还没有IE驱动
            # logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(100)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self, driver):
        logger.info("Now, Close and quit the browser.")
        driver.quit()

