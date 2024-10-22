s1='hello'
s2='world'
#1.使用+进行拼接
print(s1+s2)
#2.使用.join()进行拼接
print(''.join([s1,s2])) #'‘:不需要天加拼接字符，无间隔拼接
print('*'.join(['hello','java','python']))
print('你好'.join(['hello','java','python']))
print('你好'.join(['hello','java']))
#3.直接拼接
print('hello''world')
#4.格式化字符拼接
print('%s%s' % (s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))