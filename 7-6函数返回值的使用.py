#函数的返回值
def cale(a,b):
    print(a+b)

cale(2,0)
print(cale(1,2))

def cale2(a,b):
    s=a+b
    return s

print(cale2(1,2))
print(cale2(cale2(1,2),10))

# 返回值多个
def get_sum(num):
    s=0
    odd_num=0
    even_num=0
    for i in range(1,num+1):
        if i%2!=0: #为奇数
            odd_num+=i
        else:
            even_num+=i
        s+=i
    return odd_num,even_num,s #三个值
result=get_sum(10)
print(type(result))
print(result)

#解包赋值
a,b,c=get_sum(10) #get_sum()返回3个值，元组类型
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))