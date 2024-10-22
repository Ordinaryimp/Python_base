import random
rand=random.randint(1,100)
count=1
print(rand)
while count<=10:
    number=eval(input('请输入所猜数字(1-100之间)'))
    if number==rand:
        print('运气不错猜对了，奖励你永久性无上气运加身（限一次，后续猜对将会转化并提升你的全方面属性）')
        break
    elif number>rand:
        print('大了')
    else:
        print('小了')
    count+=1
if count<=3:
    print('厉害，追加奖励无垢圣体')
elif 3<=count<=6:
    print('还行，猜了',count,'次')
else:
    print('差点与奖励失之交臂，猜了',count,'次')
