from selenium import webdriver
from selenium.webdriver.support.ui import Select
import txtSName
import time
import datetime

sltInsuredAmout = ['100000.00', '200000.00', '300000.00', '400000.00', '500000.00']
regularBuy = webdriver.Chrome()
regularBuy.get("http://test2016.4008822300.net.cn/Regular/RegularBuyall.aspx?id=356&bid=26&dlid=9&valueid=2&price=418.00&sex=1&bir=")
for sltInsured in sltInsuredAmout:
    regularBuy.find_element_by_class_name("lg_close").click()
    regularBuy.find_element_by_class_name('mr16').click()
    regularBuy.find_element_by_class_name('gz_next').click()
    txtSName.applicant_info(regularBuy)
    txtSName.elect_id(regularBuy, 'sltProvince', '19-440000')
    txtSName.elect_id(regularBuy, 'sltCity', '246-440300')
    txtSName.elect_id(regularBuy, 'sltxian', '2336-440305')
    regularBuy.find_element_by_id('txtAddress').send_keys('科技园科苑路金融大厦19层')
    regularBuy.find_element_by_id("txtPostCode").send_keys('554400')
    txtSName.elect_id(regularBuy, 'meJob1', '1')
    txtSName.elect_id(regularBuy, 'meJob2', '1010100-1')
    regularBuy.find_element_by_id('txtMeHeight').send_keys('169')
    regularBuy.find_element_by_id('txtMeWeight').send_keys('60')
    txtSName.elect_id(regularBuy, 'sltPeriods', '7')
    txtSName.bank(regularBuy)
    regularBuy.find_element_by_id('btnpostdate1').click()
    regularBuy.implicitly_wait(3000)
    regularBuy.find_element_by_id('agree').click()
    regularBuy.implicitly_wait(4000)
    regularBuy.find_element_by_xpath(".//*[@id='divcountation2']/div[3]/div[13]/img[2]").click()
    time.sleep(3)
    texts = regularBuy.find_element_by_xpath("html/body/form/div[4]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    OrderID = texts.text
    time.sleep(2)
    regularBuy.get("http://test2016.4008822300.net.cn/Interface_Test/InterCom.aspx")
    time.sleep(2)
    regularBuy.find_element_by_id('txtSubnumber').send_keys(OrderID)
    print('金额：' + str(sltInsured) + " 订单号：" + OrderID, end=" ")
    txtSName.interfaces(regularBuy)
    regularBuy.implicitly_wait(4000)
    regularBuy.get('http://test2016.4008822300.net.cn/Regular/RegularBuyall.aspx?id=356&bid=26&dlid=9&valueid=2&price=418.00&sex=1&bir=')
regularBuy.quit()


