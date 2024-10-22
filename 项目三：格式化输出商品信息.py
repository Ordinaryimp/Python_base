lst=[
    ['01','电风扇','美的',300],
    ['02','电灯泡','恶魔',1100],
    ['03','空调机','天使',7]
]
print('编号\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()
#格式化操作
for item in lst:
    item[0]='000'+item[0]
    item[3]='￥{0:.2f}'.format((item[3]))

print('编号\t\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()


