#创建字典 字典可以包含列表、元组、字典，列表可以包含字典或元组，元组也可以包含字典或列表。这使得可以构建复杂的嵌套结构，适应各种编程需求。
a={10:'cat',20:'dog',30:'duck',40:'',10:''} #重复的键（key）值会被后面的覆盖
print(a)

lst1=[10,20,30]
lst=['cat','dog','apple','orange']
b=zip(lst1,lst)
print(b)

c=dict(b)
print(c)
#使用参数创建字典
d=dict(cat=10,dog=20)
print(d)

#字典 元组为键 10为值
t=(10,20,30)
print({t:10})

lst=[10,20,30]
#print({lst:10}) #TypeError: unhashable type: 'list' 列表为‘可变’数据类型  ‘可变’数据类型 不能作为字典中的键

#字典属于序列
print('max:',max(a))
print('min:',min(a))
print('len:',len(a))

del a
#print(a)