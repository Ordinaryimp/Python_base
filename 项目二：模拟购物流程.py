lst=[]
#录入商品信息
for i in range(5):
    lst.append(input('请输入商品编号及商品，每次只能输入一次：'))

#输出商品信息
for item in lst:
    print(item)

#创建空列表作为购物车
cart=[]
while True:
    flag=False  #代表商品不存在
    num=input('请输入要购买的商品编号：')
    for item in lst:
        if num==item[0:4]:  #切片操作,从商品中切出商品编号序号
            flag=True
            cart.append(item)
            print(item,'已成功添加到购物车')
            break #退出for循环
    if not flag and num !='q':
        print(num,'商品不存在')
    if num=='q':
        break #退出while循环
print('-'*50)
print('您的购物车里已选择的商品为：')
cart.reverse()
for item in cart:
    print(item)

