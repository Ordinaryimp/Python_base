class Car(object):
    def __init__(self,type,no):
        self.type=type
        self.no=no

    def start(self):
        print('启动！嗡~翁~~嗡~！')
    def stop(self):
        print('熄火啦')

#出租车
class Taxi(Car):
    def __init__(self,type,no,company):
        super().__init__(type,no)
        self.company=company
#重写父类的启动和停止方法
    def start(self):
        print('乘客你好！')
        print(f'我是{self.company}出租车公司，我的车牌号是{self.no},你想去哪')
    def stop(self):
        print('目的地到了，请你扫码付款，车门已自动焊死，不付款别想下车，桀桀桀')

class FamilyCar(Car):
    def __init__(self, type, no, name):
        super().__init__(type, no)
        self.name = name

    # 重写父类的启动和停止方法
    def start(self):
        print('嘿！新中国成立了，咱去哪看看哇')
        print(f'我是{self.name}同志，我的车牌号是{self.no},快开，咱一起去瞧瞧祖国的大好河山')

    def stop(self):
        print('北京到了，咱走着')
#测试
taxi=Taxi('劳斯莱斯幻影','京A888888','长城')
taxi.start()
taxi.stop()

print('-'*44)
familycar=FamilyCar('东方红拖拉机','原则','解放军')
familycar.start()
familycar.stop()



