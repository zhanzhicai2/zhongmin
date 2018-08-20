# from selenium import webdriver
from selenium import webdriver
import requests
b = webdriver.Chrome()
bg = b.git('http://www.baidu.com')
print(bg.text)
