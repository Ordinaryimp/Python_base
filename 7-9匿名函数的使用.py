def cale(a,b):
   return a+b

print(cale(10,20))

s=lambda a,b:a+b    #s表示一个匿名函数
print(type(s)) #<class 'function'>
#调用匿名函数
print(s(8,9))

#
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print()

for i in range(len(lst)):
    result=lambda x:x[i] #根据索引取值
    print(result(lst))

#
student_score=[
    {'name':'天使','score':100},
    {'name':'大额','score':120},
    {'name':'阿尔法','score':180},
    {'name':'魔咒','score':249}
]
#对列表i进行排序,排序规则 是字典中的成绩
#假设列表中有以下元素：[{'name': '天使', 'score': 100}, {'name': '大额', 'score': 120}]。
#当 sort() 开始排序时，它会：
#取第一个字典 {'name': '天使', 'score': 100} 作为 x，调用 lambda 函数，返回 100。
#取第二个字典 {'name': '大额', 'score': 120} 作为 x，调用 lambda 函数，返回 120。
#接下来，sort() 方法将使用这两个返回值（100 和 120）进行比较，以确定它们的顺序。
student_score.sort(key=lambda x:x.get('score'),reverse=True) #降序
print(student_score)