import re #导入re模块
pattern='\\d\\.\\d+'  #+限定符匹配1次或多次, \d+ 0-9 数字出现1次或多次
s='I study Python 3.11 every day' #待匹配字符
match=re.match(pattern,s,re.I)  #re.I 启用了不区分大小写的模式。
print(match)

s2='3.12pryhon I study every day'
match_2=re.match(pattern,s2)
print(match_2)
print('匹配的起始位置：',match_2.start())
print('匹配值的结束位置：',match_2.end())
print('匹配区间的位置元素：',match_2.span())
print('待匹配的字符串：',match_2.string)
print('匹配的数据：',match_2.group())
