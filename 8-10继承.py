class Person: #默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'大家好，我叫：{self.name},我今年：{self.age}岁')

#Student继承Person类
class Student(Person):
#编写初始化方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age) #调用父类的初始化方法  给子类赋值实例属性
        self.stuno=stuno
class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

#创建一个子类对象
stu=Student('小可爱',20,'1001')
stu.show()

doctor=Doctor('哇咔咔',76,'德国骨科')
doctor.show()






