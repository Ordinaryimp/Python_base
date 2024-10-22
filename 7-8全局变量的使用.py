a=100 #全局变量

def calc(x,y):
    return a+x+y
print(a)
print(calc(a,6))
print(calc(7,6))

def calc2(x,y):
    a=200       #局部变量和全局变量变量名相同时，局部变量优先级更高
    return a+x+y

print(calc2(10,20))
print(a)

def calc3(x,y):
    global s        #global s 使用s变成全局变量
    s=300
    return s+x+y
print(calc3(10,20))
print(s)
