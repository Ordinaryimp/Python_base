import re
pattern='\\d\\.\\d+'
s='I stude Python3.11 for three years python12.0 I love you'
match=re.search(pattern,s)

s2='4.10 Python I study every day'
s3='Python I study every day'
match2=re.search(pattern,s2)
match3=re.search(pattern,s3)
print(match)
print(match2)
print(match3)

print(match.group())
print(match2.group())

