from selenium import webdriver
import datetime

d1 = datetime.datetime.now()
d3 = datetime.date(d1.year, d1.month, d1.day)
d2 = d3.strftime('%Y-%m-%d')
Health = webdriver.Chrome()

