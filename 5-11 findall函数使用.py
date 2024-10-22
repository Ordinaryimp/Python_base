import re
s='I stude Python3.11 for three years python2.0 I love you'
s2='4.10 Python I study every day'
s3='Python I study every day'

pattern='\\d\\.\\d+'

lst=re.findall(pattern,s)
lst2=re.findall(pattern,s2)
lst3=re.findall(pattern,s3)

print(lst)
print(lst2)
print(lst3)