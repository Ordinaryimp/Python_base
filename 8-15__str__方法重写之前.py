class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

per=Person('城里人',18)
print(per)   #自动调用了__str__方法 输出了内存地址 报看
