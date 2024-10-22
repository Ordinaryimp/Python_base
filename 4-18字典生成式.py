import random

d={item :random.randint(-100,100) for item in range(10)}
print(d)

#创建两个列表
lst=[1001,1002,1003]
lst2=['小小','华华','天天']

d={key:value for key,value in zip(lst,lst2)}
print(d)