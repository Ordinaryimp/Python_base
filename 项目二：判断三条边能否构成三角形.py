try:
    a = eval(input('请输入三角形的第一条边：'))
    b = eval(input('请输入三角形的第二条边：'))
    c = eval(input('请输入三角形的第三条边：'))
    if a+b>c and a+c>b and c+b>a:
        print(f'三角形的边长为：{a},{b},{c}')
    else:
        raise Exception(a,b,c,'不能构成三角形')
except Exception as e:
    print(e)
