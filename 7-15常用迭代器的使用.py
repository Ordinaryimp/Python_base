lst=[54,56,77,4,567,34]

#(1)排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表:',lst)
print('升序：',asc_lst)
print('倒叙：',desc_lst)

#（2） reversed 反向
new_lst=reversed(lst)
print(type(new_lst)) #<class 'list_reverseiterator'>
print(new_lst)  #<list_reverseiterator object at 0x0000018C66FF1FF0>
print(list(new_lst))

#（3） zip
x=['a','b','c']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj)) #zip(x,y)
# print(list(zipobj))
# print(dict(zipobj))

#(4) enumerate
enum=enumerate(x,start=1)
print(type(enum)) # <class 'enumerate'>
# print(list(enum))
print(tuple(enum))

#(5)all:检测是否全是非空字符串
lst2=[10,20,'',30]
print(all(lst2))    #false
print(all(lst))     #true

#(6)any::检测是否有空字符串
print(any(lst2))

#(7)next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj))

#filter
def fun(num):
    return num%2==1
obj=filter(fun,range(10))   #将range(10),0-9的整数，都执行一次fun操作
print(list(obj))

#map
def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)    #将new_lst2内的元素都带如upper函数
print(list(obj2))