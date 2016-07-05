# 上传文件 失败 
from selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains
brweb = webdriver.Chrome()
brweb.get('http://0102.zhongmin.cn/firm/teamBuy_dazhong.aspx?id=2')
time.sleep(4)
brweb.find_element_by_xpath(".//*[@id='Login1_divLoginMask']/span").click()
time.sleep(2)
brweb.find_element_by_id.send_keys('http://images.zhongmin.cn/firm/20160627034826466.rar')
print("dddddd")