lst=[4,56,89,88,66]
print('原:',lst)

#排序
asc_lst=sorted(lst)
print('升序:',asc_lst)
print('原列表:',lst)

#降序
desc_lst=sorted(lst,reverse=True)
print('降序:',desc_lst)
print('原列表',lst)

lst2=['ban','apple','Odad','CAt']
#忽略大小写进行排序  key=str.lower属于规则：全转换为小写
new_lst2=sorted(lst2,key=str.lower)
print('原列表:',lst2)
print('排序后的列表:',new_lst2)
#sort()：就地修改原列表。
#sorted()：生成一个新的排序后的对象，不修改原始对象。

