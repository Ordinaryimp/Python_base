"""t = (i for i in range(1, 4)) 创建了一个生成器对象，而不是一个列表或其他数据结构。
#因此，当使用 print(t) 时，它只显示生成器对象的内存地址，而不会计算和输出生成器中实际的值。
如果想查看生成器的内容，需要通过迭代的方式来访问它的值，如使用 for 循环或将其转换为列表"""

t=(i for i in range(1,4))
print(t)

#t=tuple(t)
#print(t)


#遍历
#for item in t:
#    print(item)
print(t.__next__())
print(t.__next__())
print(t.__next__())
t=tuple(t)
print(t)
