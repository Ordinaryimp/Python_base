S=input('请输入一个字符串：')
def lower_upper(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32)) #将字母转成Unicode码整数，加上32 chr（）整数码转成字符
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    return ''.join(lst)     #将列表进行字符串拼接转换为字符串

#准备调用
new_s=lower_upper(S)
print(new_s)


