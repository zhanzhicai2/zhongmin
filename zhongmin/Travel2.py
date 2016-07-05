from selenium import webdriver
import time,datetime
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

# 时间+30
d1 = datetime.datetime.now()
d3 = datetime.date(d1.year,d1.month+1,d1.day)
d2 = d3.strftime('%Y-%m-%d')
def by_id(parameter_list):
    broweb.find_element_by_id(parameter_list).click()
def Id_keys(id,keys):
    broweb.find_element_by_id(id).send_keys(keys) 
broweb = webdriver.Chrome()
broweb.get('http://www.zhongmin.cn/Travel/TravelBuyNew2.aspx?id=9&day=7')
Id_keys('txtUserName','13243733102')
broweb.find_element_by_xpath(".//*[@id='txtPassWord_text']").click()
Id_keys('txtPassWord','zhan18702655166')
by_id('btnAllLogin')
time.sleep(3)
Id_keys('txtSubStart',d2)
broweb.implicitly_wait(3000)
# sname1 = ['12334','?"1"','zhanzhicai#','测试占志才1','测试占志才']
sname1 = [('12334','36068119910502219'),('?"1"','36068119910502221S'),('zhanzhicai#','360681199105022219ss'),('测试占志才1','36068119910502221X'),('测试占志才','360681199105022219')]
for value,keys in sname1:
    Id_keys('txtSName',value)
    Id_keys('txtSNo',keys)
    broweb.implicitly_wait(3000)
    broweb.find_element_by_class_name('tbrxx_tit').click()
    if value =='测试占志才' :
        x =broweb.find_element_by_id('tipBox_holdname').find_element_by_class_name('pa_ui_validator_oncorrect')
        y =broweb.find_element_by_id('tipBox_holdcard').find_element_by_class_name('pa_ui_validator_oncorrect')
    else:
        x =broweb.find_element_by_id('tipBox_holdname').find_element_by_class_name('pa_ui_validator_onerror')
        y =broweb.find_element_by_id('tipBox_holdcard').find_element_by_class_name('pa_ui_validator_onerror')
        time.sleep(2)
    print(value+"=信息："+x.text+"---"+keys+"=信息"+y.text)
    broweb.find_element_by_id('txtSName').clear()
    broweb.find_element_by_id('txtSNo').clear()