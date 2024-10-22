#三行四列
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')   #print输出会换行,用end会保持不换行且在后面加一个''(也就是空)
    print()#空行相当于换行
print('---------------')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()