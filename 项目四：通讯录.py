#创建一个空集合
s=set()
#录入5位好友的姓名和手机号
for i in range(1,6):
    info=input(f'请输入第{i}位姓名及电话号码：')
    #将数据添加到空集合中
    s.add(info)
#遍历集合
for item in s:
    print(item)
