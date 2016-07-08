from selenium import webdriver
import time

zhongmin = webdriver.Chrome()
zhongmin.get('http://www.zhongmin.cn/health/healthbuycommon.aspx?id=560&bid=12&age=0&sex=1&span=20&money=50000&payMethod=1.0000&payMethodrate=1.0000&price=372&bir=&Periods=20')
zhongmin.find_element_by_id('healNo').find_element_by_class_name('mr16').click()
