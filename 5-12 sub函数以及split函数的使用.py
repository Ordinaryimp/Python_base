import re
pattern='黑客|破解|反爬'
s='我想学习Python当黑客，破解vip视频，Prthon可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXXX',s)
print(new_s)

s2='https://cn.bing.com/search?q=mzy&form=ANNTH1'

pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)
