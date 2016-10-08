from selenium import webdriver
import time


Car = webdriver.Chrome()
Car.get('http://m02.00.com.cn/p/wap/CarLicense.aspx?ComType=8')
Car.find_element_by_id('txtCity').click()
time.sleep(2)
Car.find_element_by_id('select_city').send_keys('苏州')
time.sleep(2)
Car.find_element_by_id('divSearchCity').click()
time.sleep(2)
Car.find_element_by_id('txtLicense').send_keys('0L691')
Car.find_element_by_id('btnSure').click()
time.sleep(1)
Car.find_element_by_id('txtVName').send_keys('测试占志才')
Car.find_element_by_id('txtVCertificate').send_keys('533527198909210238')
Car.find_element_by_id('txtAMobile').send_keys('13243733102')
Car.find_element_by_id('spBusStart').click()
time.sleep(2)
Car.find_element_by_class_name('dwbw').click()
Car.find_element_by_id('btnSureOk').click()
time.sleep(3)
Car.find_element_by_id('txtFrameNo').send_keys("LSVXZ25N4F2175950")
Car.find_element_by_id('txtEngineNo').send_keys('5C1185')
Car.find_element_by_id('txtAutoModel').send_keys('大众汽车牌SVW6451EED')
Car.find_element_by_xpath(".//*[@id='page_CarAllInfor']/div/div[3]/div/ul/li[4]/span[2]").click()
# Car.find_element_by_id('divRegisterDate').click()
time.sleep(2)
Car.find_element_by_class_name('dwbw').click()
time.sleep(2)
Car.find_element_by_id('btnSure').click()


