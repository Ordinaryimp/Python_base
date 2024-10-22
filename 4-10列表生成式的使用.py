import random
list = [item for item in range(1,11)]
print(list)

list = [item*item for item in range(1,11)]
print(list)

list = [random.randint(1,100) for item in range(10)]
print(list)

list = [i for i in range(10) if i%2==0]
print(list)
