# coding=utf-8

from selenium import webdriver
import os,time

fileName=r"D:\\baidu\\ceshi2.txt"
ceshi=open(fileName, encoding="gbk")
# ceshi = open("C:\Users\Administrator\Desktop\ceshi.txt",mode='r',encoding="utf-8")
ceshidata=ceshi.readlines()
ceshi.close()


for value in ceshidata:
    brweb = webdriver.Chrome()
    brweb.get('http://www.zhongmin.cn/')
    brweb.find_element_by_id('headKey').send_keys(value)
    brweb.find_element_by_id('headKey').click()
    time.sleep(2)
    
    brweb.quit()
