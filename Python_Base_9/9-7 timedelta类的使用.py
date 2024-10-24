from datetime import datetime
from datetime import timedelta

#创建两个datetime对象

delta1=datetime(2028,10,1)-datetime(2027,5,2,4,5,6)
print('delta1的数据类型是:',type(delta1),'delta1的内容是是:',delta1)   #<class 'datetime.timedelta'>
print('2027年5月2日之后的517 days, 19:54:54为：',datetime(2027,5,2,4,5,6)+delta1)

#通过传入参数的方式创建一个timedelta对象
dt1=timedelta(10)
dt2=timedelta(10,11)
print('创建一个10天的timedelta对象',dt1)
print('创建一个10天11秒的timedelta对象',dt2)
