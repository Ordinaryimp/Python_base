class A:
    pass

class B:
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建类的对象
a=A()
b=B()
#创建c类对象
c=C('唐挨',32)
print('对象a的属性字典：',a.__dict__)   #对象的属性字典
print('对象b的属性字典：',b.__dict__)
print('对象c的属性字典：',c.__dict__)

print('对象a所属的类：',a.__class__)   #对象所属类
print('对象b所属的类：',b.__class__)
print('对象c所属的类：',c.__class__)

print('A类的父类元组：',A.__bases__)   #类的父类元组
print('B类的父类元组：',B.__bases__)
print('C类的父类元组：',C.__bases__)

print('A类的父类元组：',A.__base__)   #类的父类
print('B类的父类元组：',B.__base__)
print('C类的父类元组：',C.__base__)   #继承很多父类 结果显示第一个

print('A的层次结构：',A.__mro__)      #类的层次结构
print('B的层次结构：',B.__mro__)
print('C的层次结构：',C.__mro__)

#子类列表
print('A类的子类列表：',A.__subclasses__())
print('B类的子类列表：',B.__subclasses__())
print('C类的子类列表：',C.__subclasses__())