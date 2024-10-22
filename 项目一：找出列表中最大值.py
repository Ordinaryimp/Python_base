def get_max(lst):
    x=lst[0]
    for i in range(1,10):
        if lst[i]>x:
            x=lst[i]
    return x
import random
lst=[]
lst=[random.randint(1,100) for item in range(10)]
# for i in range(0,10):
#     lst.append(random.randint(1,100))
print(lst)
print(get_max(lst))
