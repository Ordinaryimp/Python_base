import datetime
#输入日期函数
def input_date():
    str_datetime = input('请输入开始日期，例：20251026b表示2025-10-26:')
    datestr=str_datetime[0:4]+'-'+str_datetime[4:6]+'-'+str_datetime[6:8]
    dt=datetime.datetime.strptime(datestr,'%Y-%m-%d')
    return  dt

#主程序运行
if __name__ == '__main__':
    # print(input_date())
    date=input_date()
    #输入间隔天数
    in_num=eval(input('请输入间隔天数：'))
    date=date+datetime.timedelta(in_num) #或datetime.timedelta(days=in_num)
    print('您推算的日期是：',date)