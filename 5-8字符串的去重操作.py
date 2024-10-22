s='helloworldhelloworldhelloworldllooddeaasasaa'

#拼接+not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item   #拼接操作
print(new_s)
#索引+not in
new_s=''
for i in range(len(s)):
    if s[i] not in new_s:
        new_s+=s[i]
print(new_s)
#通过集合去重+列表排序
new_s=set(s)
print(new_s)
lst=list(new_s)
print(lst)
lst.sort(key=s.index)
print(''.join(lst))

