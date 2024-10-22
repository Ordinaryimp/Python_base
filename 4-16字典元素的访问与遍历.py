a={10:'cat',20:'dog',30:'duck',40:'zoo',10:'dinner'}

#访问字典中的值 字典名[key]

print(a[10])

print(a.get(10))
print(a.get(20))
#print(a['java']) KeyError: 'java'
print(a.get('java'))

#字典遍历
for item in a.items():
    print(item) #key=value元组类型
print(item)
print(type(item))
print(type(a))

#使用for循环遍历字典时，分别获取key，value
for key,value in a.items():
    print(key,'--->',value)