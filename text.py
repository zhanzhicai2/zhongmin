# import time
# def GetNowTime():
 
#     return time.strftime("%Y-%m-%d")
# print(GetNowTime())
# # print(time.localtime(time.time())))
#-*-coding=gbk
# 时间
# import datetime,time
# def GetNowTime():
#      d1 = time.localtime(time.time())
#      d2 = d1 + time.gmtime(tm_mon=1)
#      return time.strftime("%Y-%m-%d")

# print(GetNowTime())


print(max(1,2,34,65,2,))
print(pow(3,4))
print(ord('A')) 
s = (x * x for x in range(10))
for x in s:
    print(x)
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
