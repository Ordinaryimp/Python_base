import pandas as pd
import matplotlib.pyplot as plt

#读取Excel文件
df=pd.read_excel('景区天气.xlsx')
# print(df)
#解决绘图模块中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']
#设置画布大小
plt.figure(figsize=(10,6))
labels=df['景区']
y=df['气温']
print(labels)
print(y)

#绘制饼图
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=0)    #使用之前将气温表的温度一栏删除到只留下一个温度数值，不然报错

#设置x、y轴刻度
plt.axis('equal')
plt.title('景区气温数据')

#显示出来
plt.show()
