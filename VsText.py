import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Select
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
# select = Select(driver.find_element_by_tag_name("select"))
# select.deselect_all()
# select.select_by_visible_text("Edam")

# select = Select(brower.find_element_by_tag_name("td>div>select"))
# select.deselect_all()
# select.select_by_visible_text("身份证")
sel = brower.find_element_by_xpath("//select[@id='sltSType']")
Select(sel).select_by_value('0')  #未审核



# title=brower.title
# url= brower.current_url
# handles = brower.window_handles
# Whandles = brower.current_window_handle
# print(Whandles)
# print(handles)
# print(url)
# print(title)
