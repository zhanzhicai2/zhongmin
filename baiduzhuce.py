from selenium import webdriver
# from time import sleep
import time
# import selenium

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 获取当前窗口
nowhandle = driver.current_window_handle
# print(nowhandle)
driver.implicitly_wait(3000)
# driver.find_element_by_class_name('lb').click()
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
# driver.find_element_by_css_selector('.lb').click()
driver.find_element_by_class_name('pass-reglink').click()
# driver.implicitly_wait(3000)
# driver.find_element_by_css_selector
time.sleep(5)
# driver.find_element_by_class_name('pass-reglink').click()
allhandle = driver.window_handles
print("kkkk")
for handle in allhandle:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print('now register window=',handle)
        driver.implicitly_wait(3000)
        driver.find_element_by_id('TANGRAM__PSP_4__submitWrapper').click()
        driver.implicitly_wait(3000)
        driver.close()
driver.switch_to_window(nowhandle)
driver.find_element_by_id('kw').send_keys("注册成功")


