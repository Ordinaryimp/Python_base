def fun(*para):
    print(type(para))
    for item in para:
        print(item)
#个数可变的位置参数
#调用
fun(10,20,30,40)
fun(10)
fun(10,20)
fun([10,20,30,40])  #实际上传递的是一个参数
fun({10,20,30})
fun({'a':13,'b':20})
#在调用时加一颗星，会将列表进行解包
fun(*[10,22,34,54,66,6])
print()
#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'---->',value)

#调用
fun2(name='小屁孩',age=23,height=182,IQ=249)
d={'name':'小屁孩','age':23,'height':182,'IQ':249}
fun2(**d) #TypeError: fun2() takes 0 positional arguments but 1 was given