class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show(self):
        print(f'大家好我叫{self.name},今年刚满{self.age}岁~')

#创建Person类的对象
per=Person('城里人',18)
per.show()
print(dir(per))
print(per)  #自动调用了__str__方法 输出了内存地址

