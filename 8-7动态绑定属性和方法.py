class Student:  #类名
    #类属性：定义在类中，方法外的变量
    schoool='北京XXX教育'

    #初始化方法
    def __init__(self,xm,age):
        self.name=xm    #左侧是实例属性 将局部变量xm赋给实例属性
        self.age=age

    #定义在类中的函数，称为方法，自带一个参数self

    #实例方法
    def show(self):
        print(f'我叫:{self.name},我今年{self.age}岁了')

#创建两个Student类型的对象
stu=Student('che',18)
stu2=Student('陈梅梅',20)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

# print(stu.gender)   #'Student' object has no attribute 'gender'

#动态绑定方法
def introduce():
    print('我是一个函数，我被动态绑定成了stu2对象的方法')
stu2.fun=introduce #函数的一个赋值,
#fun就是stu2对象的方法
#调用
stu2.fun()
stu2.fu1=introduce
stu2.fu1()