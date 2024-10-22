class Person():
    def Eat(self):
        print('人,吃五谷')

class Cat():
    def Eat(self):
        print('猫,吃鱼')

class Dog():
    def Eat(self):
        print('狗,吃骨头')
#三类都含有同一个方法  eat
#编写函数
def fun(obj):   #obj是函数的形式参数，在定义处知道这个形参的数据类型吗？ NO！
    obj.Eat() #通过变量obj(对象)调用eat方法

#创建三个类的对象
per=Person()
cat=Cat()
dog=Dog()

#调用fun函数
fun(per)    #Python中的多态，不关心对象的数据类型，只关心对象是否有同名方法
fun(cat)
fun(dog)
