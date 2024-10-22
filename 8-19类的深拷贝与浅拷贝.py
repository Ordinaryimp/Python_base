class CPU:
    pass
class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu;
        self.disk=disk

cpu=CPU()
disk=Disk()

com=Computer(cpu,disk)
com1=com

print(com,'子对象地址：',com.cpu,com.disk)
print(com1,'子对象地址：',com.cpu,com.disk)
#变量的赋值

#类对象的浅拷贝
import copy
print('-'*53)
com2=copy.copy(com) #com2是新产生的对象。  他的子对象cpu 和disk不变
print(com,'子对象内存地址为：',com.cpu,com.disk)
print(com2,'子对象内存地址为：',com2.cpu,com2.disk)
#类的深拷贝
print('-'*53)
com3=copy.deepcopy(com) #com2是新产生的对象。  他的子对象cpu 和disk也改变
print(com,'子对象内存地址为：',com.cpu,com.disk)
print(com3,'子对象内存地址为：',com3.cpu,com3.disk)



