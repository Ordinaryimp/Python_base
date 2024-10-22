def happy_birthday(name,age):
    print('祝'+name,end='')
    print(str(age)+'岁'+'生日快乐')
#调用
happy_birthday(age=18,name='小屁孩')
happy_birthday('坚持者',age=18) #位置传参也可以使用关键字传参
                                     #规则：位置传参在前，关键字传参在后