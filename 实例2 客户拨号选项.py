answer=(input('是否继续y/n'))
while answer=='y':
    print('------欢迎来到玛卡巴卡星球------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话时长')
    print('0.退出系统')
    number=eval(input('请输入你的选择'))
    if number==1:
        print('您当前的余额是250元整')
    elif number==2:
        print('您当前的剩余流量为10000MB')
    elif number==3:
        print('您当前的剩余通话时长为645974小时')
    elif number==0:
        print('已退出系统，祝您生活愉快')
        break
    else:
        print('输入错误，请重新输入')
        number = eval(input('请输入你的选择'))
    answer = (input('是否继续y/n'))
else:
    print('已退出系统，祝您生活愉快')

