#直接创建集合
s={1,2,3,4}
print(s)

#集合只能存储不可变数据类型
#s={[10,20],[30,40]} #TypeError: unhashable type: 'list'

#使用set创建集合
s=set() #创建一个空集合
print(s)
s={} #创建的是空字典
print(s,type(s))

s=set('HelloWorld')
print(s)

s=set([10,20,30])
print(s)

s=set(range(1,10))
print(s)

#集合属于序列的一种
print('max:',max(s))
print('min:',min(s))
print('len:',len(s))
print('9在集合中存在吗：',9 in s)
print('9在集合中不存在吗：',9 not in s)

del s
#print(s)
