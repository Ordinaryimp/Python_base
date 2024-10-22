class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这是一个外星人，具有name和age两个实例属性' #返回值是一个字符串
per=Person('城里人',18)
print(per)   #自动调用了__str__方法 输出了内存地址 报看    现 在不是了哇咔咔！
print(per.__str__())#手动调用