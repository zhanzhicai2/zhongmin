from selenium import webdriver
from time import sleep


brweb = webdriver.Chrome()
brweb.get('https://www.baidu.com/')
b=brweb.find_element_by_id('ul').find_elements_by_tag_name('a')
for value in b:
    value.click()
    sleep(2)