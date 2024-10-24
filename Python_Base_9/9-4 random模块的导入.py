#导入
import random
#设置随机数的种子
random.seed(10)
print(random.random())  #[0.0,1.0)
print(random.random())
print('-'*44)
random.seed(10)
print(random.randint(1,100))    #[1,100]

for i in range(10): #[m,n)
    print(random.randrange(1,10,3))

print(random.uniform(1,100))    #[a,b]随机小数

lst=[i for i in range(1,11)]
#从列表中随机抽
print(random.choice(lst))   #lst是列表，也称为序列

#随机排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)
