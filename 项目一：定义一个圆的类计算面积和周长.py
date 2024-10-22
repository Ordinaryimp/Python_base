r=eval(input('请输入圆的半径：'))
class Circle:
    P=3.14
    def __init__(self,r):
        self.r=r

    def area(self):
        area=self.P*pow(self.r,2)
        print('圆面积为：',area)


    def perimeter(self):
        perimeter=2*self.P*self.r
        print('周长为：',perimeter)



circle=Circle(r)
print('圆半径为：',circle.r)
circle.area()
circle.perimeter()
