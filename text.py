# from selenium import webdriver
# from time import sleep
#
#
# brweb = webdriver.Chrome()
# brweb.get('https://www.baidu.com/')
# b=brweb.find_element_by_id('ul').find_elements_by_tag_name('a')
# for value in b:
#     value.click()
#     sleep(2)
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
