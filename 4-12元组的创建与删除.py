#创建元组
t=('world',[12,34,26,'hello','牛'],'写','hhhhhh')
print(t)

print('12在该元组中是否吗',('world' in t))
print('牛在该元组中是否吗',('牛' in t))

t=tuple('helloworld')   #lst2=list('helloworld')        一个创元组一个创列表
print(t)

print('h' in t)
print('e' in t)
print('最大值是:',max(t))
print('最小值是:',min(t))
print('元组长度:',len(t))
print('t.index:',t.index('o'))
print('t.count:',t.count('o'))

#元组中只有一个元素
y=(10,)
print(y,type(y))

del y
print(y)
