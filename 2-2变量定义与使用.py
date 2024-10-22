a=8
name="好人"
#python 动态修改变量的数据类型，通过赋不同类型的值就可以直接改变数据类型
print("a的数据类型是:",type(a))
print("mame的数据类型是:",type(name))
#在python里允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(number))
print(id(no))