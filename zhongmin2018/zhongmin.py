import time
import io
import datetime
import csv
import accid
import publicmain
from selenium import webdriver
from collections import namedtuple

zhongmin_tests = webdriver.Chrome()


with open('zhongmin.csv') as zhongmin:
    zhongmin_csv = csv.reader(zhongmin)
    zhongmins = next(zhongmin_csv)
    Row_zhongmin = namedtuple('Row', zhongmins)
    for r in zhongmin_csv:
        zhongmin_row =Row_zhongmin(*r)
        url = 'https://www.zhongmin.cn/'
        case = str(zhongmin_row.Coverage)
        url_Coverage = url + case+'/detail/ip' + zhongmin_row.pid + '_is1.html'
        zhongmin_tests.get(url_Coverage)
        # case险种
        if case == 'accid':
            # url_Coverage = url + 'accid/ip' + zhongmin_row.pid + '_isl.html'
            zhongmin_tests.find_element_by_class_name('purchase-btn').click()
            warning = int(zhongmin_row.warning)
            # warning 警告层级 1 代表一层 2 代表2层
            if warning == 2:
                zhongmin_tests.find_element_by_class_name('allNo').click()
                zhongmin_tests.find_element_by_class_name('continue-btn').click()
            elif warning == 1:
                pass
            else:
                break
            # 投保人基本信息
            publicmain.applicant_info(zhongmin_tests, zhongmin_row)
            # 被保人信息
            zhongmin_tests.find_element_by_xpath('//*[@id="buyPage"]/div[1]/div[4]/div[1]/div/dl[1]/dd/div/span').click()
            r1_relation = zhongmin_row.r1_relation1
            r1_relation1 = '//*[@id="r1_Relation1"]/li[' + r1_relation + ']'
            zhongmin_tests.find_element_by_xpath(r1_relation1).click()
            # r1_relation 关系 0 代表本人 其他代表其他关系
            if r1_relation != 0:
                zhongmin_tests.find_element_by_id('r1_ChineseName1').send_keys(zhongmin_row.r1_ChineseName1)
                publicmain.identity_type_two(zhongmin_tests, zhongmin_row)
            else:
                break
            zhongmin_tests.find_element_by_id('termsOfInform').click()
            zhongmin_tests.find_element_by_id('btnpostdate1').click()
        elif case == 'travel':
            pass
        elif case == 'health':
            pass
        elif case == 'life':
            pass
        else:
            pass
        # zhongmin_tests.quit()
zhongmin.close()
