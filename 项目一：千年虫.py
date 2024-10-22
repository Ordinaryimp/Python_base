lst=[88,98,78,00,99]
print(lst)

#遍历列表
# for index in range(len(lst)):
#     if str(lst[index])=='0':
#         lst[index]='200'+str(lst[index])
#         print(lst[index])
#     else:
#         lst[index] = '19' + str(lst[index])
#         print(lst[index])
# print('修改后的列表',lst)

for index,value in enumerate(lst):
    if str(value)=='0':
        lst[index]='200'+str(lst[index])
    else:
        lst[index] = '19' + str(lst[index])
print('修改后的列表',lst)
# for item in lst:
#     if item==0:
#         print(item+2000)
#     else:
#         print(item+1900)
