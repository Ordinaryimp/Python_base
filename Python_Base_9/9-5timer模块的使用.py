import time
now_t=time.time()
print(now_t)

obj=time.localtime()    #struct_time
print(obj)

obj2=time.localtime(60)     #60秒    1970年 1月1日 8时 ‘1分‘ ’秒
print(obj2)
print(type(obj2))
print('年份:',obj2.tm_year)
print('月份:',obj2.tm_mon)
print('月份:',obj2.tm_hour)
print('月份:',obj2.tm_min)
print('月份:',obj2.tm_sec)
print('星期：',obj2.tm_wday)   #[0,6]  3表示星期四
print('今年的多少天：',obj2.tm_yday)
print(time.ctime()) #时间戳所对应的易读的字符串 Wed Oct 23 09:15:07 2024

#日期时间格式化                                                                          格式化
print(time.strftime('%Y-%m-%d',time.localtime()))   #年月日    #str 字符串  f--->format ---time时间
print(time.strftime('%H:%M:%S',time.localtime()))   #时分秒
print('%B月份的名称：',time.strftime('%B',time.localtime()))
print('%A星期的名称：',time.strftime('%A',time.localtime()))

#字符串转成struct_time对象
print(time.strptime('2008-08-08','%Y-%m-%d'))
#延时
time.sleep(3)  #延时20s  如果需要更高精度的延时，可以考虑使用更专业的定时库，
print('helloworld')                   # 如 threading.Timer 或 asyncio 等，但通常情况下，time.sleep() 足以满足大多数需求。


