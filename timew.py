# import datetime
#
# d1 = datetime.datetime.now()
# d2 = d1+datetime.timedelta(days=1)
# # d3 = datetime.date(d1.year,d1.month+1,d1.day)
# # d2.strftime('%Y-%M-%S')
#
# # a, b, c = 0, 0, 0
#
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000-a-b
#         if a**2+b**2 == c**2:
#             print(a, b, c)
#
# l = [3, 5, 67, 7, 5, 2, 0]
# listed = l.sort()
# print(l)
# # print(list.sorted())

def func():
   for i in xrange(10):
        yield i

# [i for i in xrange(10)]