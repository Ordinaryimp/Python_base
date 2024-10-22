try:
    gender=input('请输入您的性别:')
    if gender!='男'and gender!='女':
        raise  Exception('性别只能是男或者女')
    else:
        print('天字号{0}士一位！'.format(gender))
        print(f'天字号{gender}士一位！')
        print('天字号%s士一位！' % gender)
except Exception as e:
    print(e)