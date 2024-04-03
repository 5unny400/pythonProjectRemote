"""
@FileName：10merge.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./2.jpg")
img_cat = cv.imread("./1.jpg")
# 设置与 img 一样的数值
img_cat = cv.resize(img_cat,(718,282))
# 设置宽度值
res = cv.addWeighted(img,0.4,img_cat,0.6,0)

# 图像显示
plt.imshow(res)
plt.show()