s1="HelloWorld"
new_s1=s1.replace('o','你好',1)   #最后一个参数是替换次数，默认全部替换
print(new_s1)

#字符串在指定的宽度范围内居中
print(s1.center(20))
print(s1.center(20,'*')) #用*填充

#默认去掉字符串左右的空格  若有参数会删除指定的字符集合中的字符，且是从字符串的两端删除，不会影响字符串中间的字符。如果你需要删除特定字符或空白字符
s='   Hello   World  y'
print(s.strip())    #删除字符串两端的空白字符（包括空格、制表符和换行符）’
print(s.lstrip())   #去左
print(s.rstrip())   #去右

#去指定字符串
s2='ab_dadwqffba'
print(s2.strip('ab'))
print(s2.strip('ba'))
print(s2.lstrip('ba'))
print(s2.rstrip('ba'))

