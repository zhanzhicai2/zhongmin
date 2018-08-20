# from typing import List
# 测试


class ClassA(object):
    stringA = '这是一个字符串'

    def instancefunc(self):
        print('这是一个实例方法')
        print(self)

    @classmethod
    def class_func(cls):
        print('这是一个实例方法')
        print(cls)

    @staticmethod
    def static_fun():
        print('这是实例方法')


test = ClassA()
test.instancefunc()
test.static_fun()
test.class_func()
print(test.stringA)
ClassA.static_fun()
ClassA.class_func()
ClassA.instancefunc(test)
ClassA.instancefunc(ClassA)
