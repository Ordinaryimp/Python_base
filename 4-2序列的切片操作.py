s='HelloWorld'

s1=s[0:5:2]
print(s1)
#省略开始位置
print(s[:5:1])
#省略开始与步长
print(s[:5:])
#省略结尾
print(s[5::1])
#省略结尾与步长
print(s[0::])
print(s[0:])
#省略开始与结尾
print(s[::2])
#步长为负数      逆序
print(s[::-1])
print(s[-1:-11:-1])