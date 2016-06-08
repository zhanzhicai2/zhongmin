import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from selenium import webdriver
from time import sleep
# 输出乱码
brower = webdriver.Chrome()
brower.get("http://www.zhongmin.cn/accid/Product/accident348.html/")
brower.implicitly_wait(100000)
# brower.find_element_by_id("headKey").send_keys("华夏关爱宝")
b=brower.find_element_by_id("abuyurl1").click()
brower.find_element_by_class_name("lg_close").click()
brower.implicitly_wait(30000)
brower.find_element_by_class_name("mr16").click()
brower.implicitly_wait(30000)
brower.find_element_by_class_name("gz_next").click()
brower.find_element_by_id("txtSubStart").send_keys("2016-06-12")
brower.find_element_by_id("txtSName").send_keys("测试占志才")
# select=brower.find_element_by_id("sltSType")
# select.iselectByVisibleText(“身份证”)
brower.find_element_by_id("sltSType").click()






# title=brower.title
# url= brower.current_url
# handles = brower.window_handles
# Whandles = brower.current_window_handle
# print(Whandles)
# print(handles)
# print(url)
# print(title)
