import numpy as np
import matplotlib.pyplot as plt

#读取图片
n1=plt.imread('qq.png')
print(type(n1),n1)  #数组类型 三维数组  高维表示高 次高维表示宽 低维表示[R G B]颜色
plt.imshow(n1)

#编写一个灰度处理公式
n2=np.array([0.299,0.587,0.114])    #创建数组

#将数组n1（RGB）颜色值与数组n2(灰度公式固定值)，进行点乘运算
# x=np.dot(n1,n2) #jpg图像
x=np.dot(n1[...,:3],n2) #png图像

# 传入数组 显示灰度
plt.imshow(x,cmap='gray')
#显示图像
plt.show()


