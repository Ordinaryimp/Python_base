#遍历字符串
for i in 'hello':
    print(i)
#range()函数：Python的内置函数，产生一个[n,m]的整数序列,包含n,但不包含m

for i in range(1,11):
    #print(i)
    if i%2==0:
      print(i,'是偶数')

#计算1-10之间的累加和
s=0
for i in range(1,11):
    s+=1
print('1-10之间的累加和为：',s)
print('求100-999之间的水仙花数')

for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    hundred=i//100
    if sd**3+tens**3+hundred**3==i:
        print('水仙花数有：',i)