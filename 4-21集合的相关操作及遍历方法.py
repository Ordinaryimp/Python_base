s={10,20,30}

#添加元素
s.add(100)
print(s)

#去除元素
s.remove(10)
print(s)

#随机删除一个元素
print(s.pop())
print(s)

#清空集合中的元素
s.clear()
print(s)

#遍历集合
s1={10,20,30}
for item in s1:
    print(item)

for index,item in enumerate(s1):
    print(index,item)

s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==0}
print(s)