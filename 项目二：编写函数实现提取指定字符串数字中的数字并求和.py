S=input('请输入字符串:')
def get_digit(x):
    s=0 #存储累加和
    lst=[] #存储提取出来的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
            s+=int(item)
    print('提取的数字有：',lst)
    print('累加和为：',s)
get_digit(S)

S=input('请输入字符串:')
def get_digit(x):
    s=0 #存储累加和
    lst=[] #存储提取出来的数字
    for item in x:
        if item.isdigit():
            lst.append(int(item))
    s=sum(lst)
    return lst,s
get_digit(S)
lst,s=get_digit(S)
print('数字列表为：',lst)
print('数字累加和为：',s)

