print('非空字符串的布尔值',bool('hello'))
print('空字符串的布尔值：',bool(''))
print('空列表的布尔值：',bool([]))
print('空列表的布尔值：',bool(list()))
print('空元组的布尔值：',bool([]))
print('空元组的布尔值：',bool(tuple()))
print('空集合的布尔值：',bool(set()))
print('空字典的布尔值：',bool({}))
print('空字典的布尔值：',bool(dict()))
print('-'*30)
print('非零数值型的布尔值',bool(123))
print('整数0的布尔值',bool(0))
print('浮点数0的布尔值',bool(0.0))

#将其他类型转化为字符串类型
print()
lst=[10,20,30]
print(type(lst),lst)
s=str(lst)
print(type(s),s)

#float和str转化为int类型
print('-'*30,'float类型和str类型转成int类型','-'*30)
print(int(3.14)+int('91'))
a='09'
print(int(a))

print('-'*30,'int类型和str类型转成float类型','-'*30)
print(float(31)+float(88))

seq=range(1,10)
print(tuple(seq))
print([seq])
print(set(seq))
print(list(seq))