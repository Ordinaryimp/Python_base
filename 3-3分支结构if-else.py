number=eval(input('请输入您的6位中奖号码：'))

if number==987654:
    print('恭喜您中奖了')
else:
    print('很遗憾你没中奖')
#以上可以使用条件表达式简化
result="恭喜你中奖了！"if number==987654 else "您未中本次大奖"
print(result)
