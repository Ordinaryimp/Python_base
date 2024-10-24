import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name,id(a),id(my_info))     #没有开辟内存空间
a.info()

#(2)from……import
from my_info import name #导入的是一个具体的变量名称
print(name)

#info()

from my_info import info #导入的是一个具体的函数的名称
info()

#通配符
from my_info import *   #'*'导入这个模块的所有
print(name)
info()

#同时导入多个模块
import match,time,random   #存在同名变量或者函数   后导入会对前导入进行覆盖




