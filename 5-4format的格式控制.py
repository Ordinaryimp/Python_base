s='HelloWorld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
#0：format中的第一个参数 :引导符 *:空白部分由*填充 <:左对齐 ^:中间对其 >:右对齐

#另一种居中对齐
print(s.center(20,'*'))

#千位分隔符(只适用于整数和浮点数) 三位一逗
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.1139))

#浮点数小数部分的精度
print('{0:.2f}'.format(3.1415026))
#字符串类型，表示是最大的显示长度
print('{0:.5s}'.format('Helloworld'))

#整数类型
a=425
print('二进制:{0:b},十进制{0:d},八进制{0:o},十六进制{0:x},十六进制{0:X}'.format(a))

#浮点数类型
b=3.14159
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))