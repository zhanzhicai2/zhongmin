import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# from selenium import webdriver
from selenium import webdriver
# from time import sleep


from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Select
# 输出乱码
brower = webdriver.Chrome()
brower.get("http://www.zhongmin.cn/Travel/TravelBuyNew2.aspx?id=567&day=7")
brower.implicitly_wait(100000)
# brower.find_element_by_id("headKey").send_keys("华夏关爱宝")
b=brower.find_element_by_id("abuyurl1").click()
brower.find_element_by_class_name("lg_close").click()
brower.implicitly_wait(30000)
brower.find_element_by_class_name("mr16").click()
brower.implicitly_wait(30000)
brower.find_element_by_class_name("gz_next").click()
brower.find_element_by_id("txtSubStart").send_keys("2016-07-12")
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
brower.find_element_by_id('txtSNo').send_keys('110101198106013496')
brower.implicitly_wait(30000)
brower.find_element_by_id('txtSPhone').send_keys('13243733102')
brower.find_element_by_id('txtSEmail').send_keys('zhanzhicai@zhongmin.net.cn')
sel1 = brower.find_element_by_xpath("//select[@id='meJob1']")
Select(sel1).select_by_value('1')
sel2 = brower.find_element_by_xpath("//select[@id='meJob2']")
Select(sel2).select_by_value('23')
sel3 = brower.find_element_by_xpath("//select[@id='meJob3']")
Select(sel3).select_by_value('000101-1')
brower.find_element_by_id('btnpostdate1').click()
brower.find_element_by_id('agree').click()
brower.find_element_by_id('imgBuy').click()
brower.find_element_by_id('dd')
