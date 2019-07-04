import numpy as np
from PIL import Image
import scipy.signal as signal

img = Image.open('lanna.jpg')
data = []
#读取照片建立对象
width,height = img.size
#记录尺寸
#读取图像的值
#记录每一行像素
#读取每一行像素
#用getpixel
#把行元素加入到row中去在将row中的元素添加到data的尾部
#建立模拟的二维list
for h in range(height):
    row = []
    for w in range(width):
        value = img.getpixel((w,h))
        row.append(value)
    data.append(row)
data = signal.medfilt(data,(3,3,1))#二维中值滤波
data = np.int32(data)#转换为int类型快速使用二维滤波

print(data)
for h in range(height):#对每一行
    for w in range(width):#对该行的每一列
        img.putpixel((w,h),tuple(data[h][w]))#将data中该位置的值存进图像，要求参数为tuple
img.save("result.jpg")#存储