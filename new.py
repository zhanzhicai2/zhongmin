# class Test:
#     def __init(self):
#       pass
#
#     def f(self):
#       print('Hello, World!')
#
# if __name__ == '__main__':
#   Test().f()
# 深拷贝浅拷贝


import copy

alist = [1, 2, 3, [12, 4]]

# alist = (1, 2)

b = alist
print(alist)
print(b)
print(id(b))
print(id(alist))


# 浅拷贝


b_copy = copy.copy(alist)
alist[3].append(455)
print(alist)
print(b_copy)
print(id(b_copy))
print(id(alist))

d_copy = copy.deepcopy(alist)
print(alist)
print(d_copy)
print(id(d_copy))
print(id(alist))
