#二维列表的创建
import random
lst=[
    ['城市','环比','同比'],
    ['北京','100','344'],
    ['上海','321','122'],
    ['四川','786','1373']
]
print(lst)

#遍历二维列表
for row in lst:    #行
    for item in row:    #列
        print(item,end='\t')
    print()

#列表生成式生成一个4行5列二维列表
lst2=[ [j for j in range(5)] for i in range(4)]
print(lst2)

lst2=[ [random.randint(1,100)] for i in range(4)]
print(lst2)

