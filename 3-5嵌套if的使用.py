answer=input('请问，你喝酒了吗')
if answer=='y':
    proof=eval(input('请输入酒精含量:'))
    if proof<20:
        print('走吧，臭小子')
    elif proof<80:
        print('你被捕了!臭喝酒的!')
    else:
        print('击毙你，小子！')
else:
    print('一边玩去，这没你的事')