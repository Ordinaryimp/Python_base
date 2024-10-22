data=eval(input('请输入要匹配的数据:'))
match data:
    case{'name':'mzy','age':22}:
        print('字典')
    case[12,31,41,'李白']:
        print('列表')
    case(10,20,'杜甫'):
        print('元组')
    case _:
        print('都不匹配')
