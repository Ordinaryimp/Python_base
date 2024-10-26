import jieba
#常用于人工智能的自然语言断句
with open('华为三折叠.txt','r',encoding='utf-8') as file:
    s=file.read()
#print(s)
#分词
lst=jieba.lcut(s)
print(lst)

#文本去重操作
set1=set(lst) #使用集合去重

#统计词出现频率
d={}    #key:词，value:出现的次数
for item in set1:
    if len(item)>=2:    #统计字数大于等于2的词
        d[item]=0

# print(d)
for item in lst:
    if item in d:
        d[item]=d.get(item)+1

# print(d)
new_lst=[]
for item in d:
    new_lst.append([item,d[item]])
print(new_lst)

#列表排序
print()
new_lst.sort(key=lambda x:x[1],reverse=True)    #根据出现次数降序排序
print(new_lst[0:10])    #显示排名前十项

input()


