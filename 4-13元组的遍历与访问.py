t=('python','hello','world')
#根据索引访问元组
a,b,c=t
#解包元组赋值
print(a)
print(b)
print(c)
print(t[0])
t2=t[0:3:2]
print(t2)

for item in t:
    print(item)

#for+range()+len()
for i in range(len(t)):
    print(i,t[i])

for index,item in enumerate(t):
    print(index,'--->',item)

for index,item in enumerate(t,start=66):
    print(index,'--->',item)

