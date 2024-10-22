try:
    score=eval(input('请输入成绩'))
    if 0<=score<=100:
        print('分数为：', score)
    else:
        raise Exception('成绩不正确')
except Exception as e:
    print(e)





