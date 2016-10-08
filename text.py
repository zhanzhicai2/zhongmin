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
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())


# def fib(n):
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     # print()
#     print("xiexie")
#
# x = 1
# while x < 10:
#     x = x * 2
#     print(x, end=' ')
# print(x)
# fib(10)

# del x.counter

# def fib2(n):
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     print(result)
#
#
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# fib(9)
# fib2(30)
# def funA(a, *b):
#     print(a)
#     print(b[1])
# funA(100, 99, 334, 333)
#
#
# def funB(a, **b):
#     print(a)
#     print(b)
# funB(122, b=23)
#
#
# def funC(a, **b):
#     print(a)
#     for x in b:
#         print(b[x])
#         print(x+":"+str(b[x]))
#
#
# funC(122, p=34, b=23, h=89)

def fab(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

for i in fab(20):
    print(str(i)+',')
    # print(str(i) + ',', end='')



































