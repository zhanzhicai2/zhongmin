import time
from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': 'N2F4C15C18024017',

                'platformVersion': '6.0.2',

                # apk包名

                'appPackage': 'com.zhongmin.lingling',

                # apk的launcherActivity

                'appActivity': 'com.zhongmin.lingling.SplashActivity'
                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
