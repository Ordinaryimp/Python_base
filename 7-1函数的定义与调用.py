def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的累加和为：{s}')

#函数的调用
get_sum(10) #1-10之间的累加和
get_sum(100)  #1-100之间的累加和
get_sum(1000)  #1-1000之间的累加和
get_sum(10000)  #1-10000之间的累加和

