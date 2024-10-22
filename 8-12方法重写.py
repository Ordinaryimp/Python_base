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
    def show(self):
        #调用父类的方法
        super().show()
        print(f'我来自庞各庄大学，我的学号是：{self.stuno}')

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

    def show(self):
        # super().show()
        print(f'大家好，我叫：{self.name},我今年：{self.age}岁,我是专业的{self.department}主治医生')

#创建一个子类对象
stu=Student('小可爱',20,'1001')
stu.show()

doctor=Doctor('哇咔咔',76,'德国骨科')
doctor.show()