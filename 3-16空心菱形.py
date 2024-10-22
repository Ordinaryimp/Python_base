row=eval(input('请输入菱形行数'))
while row%2==0:
    print('请重新输入')
    row = eval(input('请输入菱形行数'))
#上半部分
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,row+1-2*i):
        if k == 1 or k == row+1-2*i-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()