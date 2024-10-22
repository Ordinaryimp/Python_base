s='我爱学习,12ad1学习爱我'
#编码 str->bytes
scode=s.encode(errors='replace') #编码默认utf-8编码 utf-8 一个中文占三个字节
print(scode)
s='我爱学习学习爱我'
scode=s.encode(errors='replace')
print(scode)

scode_GBK=s.encode('GBK',errors='replace') #GBK编码 一个中文占2个字符
print(scode_GBK)
print()
#编码中的出错问题
s2='你好✌'
scode_error=s2.encode('gbk',errors='ignore')  #忽略错误
print(scode_error)
scode_error=s2.encode('gbk',errors='replace')  #无法转换就用？替换
print(scode_error)
print()
#解码过程 bytes->str
print(bytes.decode(scode_GBK,'gbk'))
print(bytes.decode(scode,'utf-8'))


#scode=s2.encode('gbk',errors='strict')  #严格模式 有错就报错
