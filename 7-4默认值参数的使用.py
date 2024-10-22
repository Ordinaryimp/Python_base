def happy_birthday(name='小屁孩',age=18):
    print('祝'+name,end='')
    print(str(age)+'岁'+'生日快乐')

happy_birthday()
happy_birthday('我自己')
happy_birthday(age=26) #关键字传参, name没传 采用默认值

def fun(a,b=20):   #a作为位置参数，b作为默认值参数
    pass
# def fun(a=10, b): #报错 位置参数 默认值参数 同时存在时，默认值参数在后