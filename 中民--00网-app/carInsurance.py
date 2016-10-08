from selenium import webdriver
import time


carDevices = webdriver.Chrome()

carDevices.get("http://m01.00.com.cn/p/wap/CarLicense.aspx?ComType=10")

carDevices.find_element_by_id("txtCity").click()
time.sleep(2)
carDevices.find_element_by_id("select_city").send_keys("沈阳")
time.sleep(2)
carDevices.find_element_by_xpath("html/body/form/section[2]/div[3]/ul/li[1]").click()
time.sleep(2)
carDevices.find_element_by_id("txtLicense").clear()
carDevices.find_element_by_id("txtLicense").send_keys("辽A14528")
carDevices.find_element_by_id("btnSure").click()
carDevices.implicitly_wait(2000)
carOwnersInfo = {"txtVName": "测试占志才", "txtVCertificate": "110101198005010253", "txtAMobile": "13243733102"}
for keys, value in carOwnersInfo.items():
    carDevices.find_element_by_id(keys).send_keys(value)
carDevices.find_element_by_id("spBusStart").click()
time.sleep(1)
carDevices.find_element_by_class_name("dwb").click()
carDevices.find_element_by_id("btnSureOk").click()

carInfo = {"txtFrameNo": "LFV2A1BS1D6094860", "txtEngineNo": "H45060", "txtAutoModel": "TV7163GLM5"}
for keys, value in carInfo.items():
    carDevices.find_element_by_id(keys).send_keys(value)

carDevices.find_element_by_id("spRegisterDate").click()
time.sleep(1)
carDevices.find_element_by_class_name("dwb").click()
carDevices.find_element_by_id("btnSure").click()
time.sleep(5)
carDevices.find_element_by_xpath("html/body/form/section[2]/div/fieldset/div[2]/div/div[2]/label/span[1 ]").click()
carDevices.implicitly_wait(2000)
carDevices.find_element_by_id("btnSureCarAuto").click()



