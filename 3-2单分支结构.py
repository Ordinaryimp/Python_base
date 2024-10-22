x=6
y=7
number=(eval(input('请输入中奖号码')))
n=98
if number==987654321:
    print('恭喜你中奖了')
if number != 987654321:
    print('很遗憾你没中奖了')
if  n%2:
    print(n,'是奇数')
if not n%2:
    print(n, '是偶数')
#判断空字符串
x=input('请输入一个字符串')
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')
a=10
b=6
if a>b:max=a
print('最大值是：',max)
min=6 if 6<7 else 7
print(min)