"""
@FileName：09border.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""
# 导入 OpenCV 库
import cv2 as cv
# 导入 maplotlib
import matplotlib.pyplot as plt

img = cv.imread("./1.jpg",)
# 定义图片显示大小
top_size,buttom_size,left_size,right_size = (50,50,50,50)
# 复制法，也就是复制最边缘像素
replicate = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)

# 反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcbajabcdefghjhgfedcb
reflect = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REFLECT)
# 反射法，也就是以最边缘像素为轴、对称、gfedcbjabcdefghigfedcba
reflect01 = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_REFLECT_101)
# 外包装法 cdeifghjabcdefghjabcdefg
wrap = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_WRAP)
# 常量法，常数值填充
constant = cv.copyMakeBorder(img,top_size,buttom_size,left_size,right_size,borderType=cv.BORDER_CONSTANT)
# 设置图像位置
plt.subplot(231)
# 设置图像显示
plt.imshow(img,'gray')
# 设置标题
plt.title('ORIGINAL')

plt.subplot(232)
plt.imshow(replicate,'gray')
plt.title("REPLICATE")

plt.subplot(233)
plt.imshow(reflect,'gray')
plt.title("REFLECT")

plt.subplot(234)
plt.imshow(reflect01,'gray')
plt.title("REPLICATE01")

plt.subplot(235)
plt.imshow(wrap,'gray')
plt.title("WRAP")

plt.subplot(236)
plt.imshow(constant,'gray')
plt.title("CONSTANT")
# 图像显示
plt.show()
