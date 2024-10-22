class Student:  #类名
    #类属性：定义在类中，方法外的变量
    schoool='北京XXX教育'

    #初始化方法
    def __init__(self,xm,age):
        self.name=xm    #左侧是实例属性 将局部变量xm赋给实例属性
        self.age=age

    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫{self.name},我今年{self.age}岁了')

    #静态方法
    @staticmethod
    def sm():
        # print(self.name)
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')
    @classmethod
    def cm(cls): #cls-->class的简写
         print('这是一个类方法。不能调用实例属性，也不能调用实例方法')
#创建类的对象
stu=Student('chy',18)   #为什么传两个参数，因为__init__方法中，有两个形参，self是自带参数。无需手动传入
#实例属性，使用对象名进行打点调用的
print(stu.name,stu.age)
#类属性，直接使用类名，打点调用

print(Student.schoool)

#实例方法，使用对象名进行打点调用
stu.show()

#类方法,@staticmethod进行修饰的方法，直接使用类名打点调用
Student.cm()

#静态方法@staticmethod进行修饰的方法，直接使用类名打点调用
Student.sm()


