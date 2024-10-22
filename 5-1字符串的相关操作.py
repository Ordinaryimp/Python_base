#大小写转换
s1="HelloWorld"
new_s1=s1.lower()
print(new_s1)
new_s1=s1.upper()
print(new_s1)

#字符串分割
e_mail='abc@1086.com'
lst=e_mail.split('@')
print(lst)
print('邮箱名：',lst[0],'邮箱服务器域名:',lst[1])

#统计字符出现次数
print(s1.count('o'))

#检索操作
print(s1.find('o'))
print(s1.find('p')) #-1 表示不存在
print(s1.index('o'))

#判断前缀和后缀
print(s1.startswith('H'))
print('demo.py'.startswith('d'))
print('demo.py'.startswith('d'))
print('demo.py'.endswith('.py'))
print('text.py'.endswith('.py'))