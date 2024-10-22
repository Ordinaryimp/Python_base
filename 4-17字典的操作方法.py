d={1001:'小明',1002:'小红',999:'小兰',777:'小蓝'}
print(d)
print(type(d))
d[1003]='小绵羊'
print(d)

#获取字典的键
keys=d.keys()
print(keys)
print(type(keys))
print(list(keys))
print(tuple(keys))

#获取字典的值
values=d.values()
print(values)
print(type(values))
print(list(values))
print(tuple(values))

##获取字典的键值对 元组形式
lst=d.items()
print()
print(lst)
print(type(lst))

#删除元素
print(d.pop(777))
print(d)
print(d.pop(888,'不存在'))

#随机删除 3.7版本后字典被归类为有序 只删除最后一个键值对
print(d.popitem())
print(d)

#清空字典
d.clear()
print(d)

print(bool(lst))#此时为d空故为false
# lst 是一个动态的视图对象，而不是一个静态的副本。当执行 lst = d.items() 时，lst 实际上是引用了字典 d 的视图。也就是说：
#动态视图：lst 是对字典 d 的动态视图，它会实时反映 d 的状态。任何对 d 的修改（如添加、删除键值对）都会立即影响 lst。

print(bool(d))
#python中一切皆对象，每个对象都有一个布尔值



