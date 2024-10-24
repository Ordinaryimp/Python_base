import admin.my_admin as a  #包名.模块名 admin:包名 my_admin：模块名
a.info()

print('-'*44)
from admin import my_admin as b #from 包名 impoort模块名 as 别名
b.info()

from admin.my_admin import info #from 包名 impoort模块名 import 函数/变量等
info()

from admin.my_admin import *    #from 包名 impoort模块名 import *
print(name)