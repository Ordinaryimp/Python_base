i=0;
while i<3:
    user_name=input('请输入您的用户名')
    pwd=input('请输入您的密码：')
    if user_name=='mzy' and pwd=='666':
        print('系统正在登陆,请稍后...')
        i=8 #用户密码正确的情况
    else:
        if i<2:
            print('用户名密码不正确,您还有',2-i,'次机会')
        i+=1#相当于i=i+1
if i==3:    #当输入3次不正确时循环结束了
    print('臭盗号的别特么试了，滚！')
