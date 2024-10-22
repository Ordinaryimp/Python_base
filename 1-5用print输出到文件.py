fp=open('note.txt','w')          #打开文件 w--write
print('北京欢迎你',file=fp)     #将北京欢迎你字符串写入到note.txt文件中，即fp中
fp.close()  # 关闭文件