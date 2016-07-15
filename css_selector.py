from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

brweb = webdriver.Chrome()
brweb.get('http:/www.zhongmin.cn')
time.sleep(5)
md = brweb.find_element_by_css_selector('.subnav-item')
ActionChains(brweb).move_to_element(md).perform()

brweb.find_element_by_xpath(".//*[@id='form1']/div[7]/div[3]/div/div[1]/div/ul/li[1]/div[2]/div[2]/ul/li[1]/a").click()
# brweb.find_element_by_class_name('subnav-tit').click()
