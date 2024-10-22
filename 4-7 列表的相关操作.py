lst=['hello','world','python','php']
print('原列表',lst,id(lst))
#增加列表元素
lst.append('sal')
print('增加元素之后:',lst,id(lst))

#使用insert(index,x)在指定的index位置上插入元素100
lst.insert(1,100)
print(lst)

#列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表:',lst,id(lst))
#使用pop(index)根据索引将元素取出,然后再删除
print(lst.pop(1))
print(lst)

#列表的反向输出
lst.reverse()#列表反转
print(lst)

#列表的拷贝,将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(lst)
print(new_lst,id(new_lst))
print(new_lst)
#列表元素的修改操作
#根据索引进行修改元素
lst[1]='my'
print(lst)

#清除列表中的所有元素clear()
lst.clear()
print(lst,id(lst))#删除后变成空列表