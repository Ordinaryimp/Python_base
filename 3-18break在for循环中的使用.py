for i in 'hello':
    if i=='e':
        break
    print(i)
print('__________')
for i in range(3):
    user_name = input('请输入用户名：')
    pwd = input('请输入密码:')
    if user_name == 'mzy' and pwd == '666':
        print('系统正在登陆，请稍后')
        break
    else:
        if i < 2:
            print('用户名或密码不正确，你还有', 2 - i, '次机会')
else:
    print('三次均错误')