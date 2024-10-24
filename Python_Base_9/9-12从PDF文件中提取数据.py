import pdfplumber

#打开PDF文件
with pdfplumber.open('python文档.pdf') as pdf:
    for i in pdf.pages: #遍历PDF页码
        print(i.extract_text()) #extract_text()提取内容
        print(f'--------------第{i}页提取结束')
