lst=[4,56,89,88,66]
print('原:',lst)

#排序默认是升序
lst.sort() #排序在原列表基础上排序不会产生新列表对象
print('升序',lst)

#排序，降序
lst.sort(reverse=True)
print('降序：',lst)
print('--------------')
lst2=['ban','apple','Odad','CAt']
print('原列表',lst2)

#升序，先排大写再，后排小写
lst2.sort()
print('升序',lst2)

#降序，先排小写再，后排大写
lst2.sort(reverse=True)
print('降序',lst2)

#忽略大小写进行比较
#lst2：这是需要排序的列表。
#.sort()：这是一个列表的方法，用于就地排序列表中的元素。
#key=str.lower：这是一个可选参数，指定排序的关键字函数。
# 在这里，str.lower 函数将列表中的每个元素转换为小写，以此作为排序的依据。
# 这意味着在排序时，大小写不再影响元素的相对顺序。
lst2.sort(key=str.lower)#全转化为小写
print(lst2)
