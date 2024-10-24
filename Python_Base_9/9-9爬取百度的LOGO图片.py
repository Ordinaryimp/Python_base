import requests
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

resp=requests.get(url)

#保存本地看一下
with open('logo.png','wb')as file:
    file.write(resp.content)    #resp.content 响应结果的二进制数据
