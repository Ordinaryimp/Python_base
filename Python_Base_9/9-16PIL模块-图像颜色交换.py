from PIL import Image
#加载图片
im=Image.open('qq.jpg')
# print(type(im),im)  #<class 'PIL.PngImagePlugin.PngImageFile'>
                    # <PIL.PngImagePlugin.PngImageFile image mode=RGBA size=100x100 at 0x12076A12390>
#提取RGB图像的颜色通道，返回结果是图像的副本
r,g,b=im.split()
print(r)
print(g)
print(b)
