import datetime

d1 = datetime.datetime.now()
d2 = d1+datetime.timedelta(days=1)
d3 = datetime.date(d1.year,d1.month+1,d1.day)
d2.strftime('%Y-%M-%S')
print(d2)
print(d3)