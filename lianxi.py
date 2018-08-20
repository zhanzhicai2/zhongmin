classmates = ['Michael', 'Bob', 'Tracy']
b= classmates[1] = 'dog'
# 增加 删除
classmates.append("zhan")
c= classmates.insert(1,'mod')
classmates.pop(2)
print(classmates)
# tuple 云祖
t = (1,)
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')


def fun1(names):
    print "fun1"
def fun2(nameb):
    test()
    print "fun2"

@fun2
def test():
    print "test()"