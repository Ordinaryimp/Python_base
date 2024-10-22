s='HelloWorld'
print('e在HelloWorld中存在吗?',('e'in s))
print('v在HelloWorld中存在吗?',('v'in s))
#not in
print('e在HelloWorld中存在吗?',('e'not in s))
print('v在HelloWorld中存在吗?',('v'not in s))

#内置函数使用
print('len():',len(s))
print('max():',max(s))      #按ACLLS码比较
print('min():',min(s))

#序列对象的方法
print('s.index():',s.index('o'))
#print('s.index():',s.index('v'))    #不存在会报错
print('s.count():',s.count(('l')))