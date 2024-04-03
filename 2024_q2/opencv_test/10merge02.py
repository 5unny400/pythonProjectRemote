"""
@FileName：10merge02.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

import cv2 as cv

img = cv.imread("./2.jpg")
img_cat = cv.imread("./1.jpg")
print(img.shape)
# 设置与 img 一样的数值
img_cat = cv.resize(img_cat,(718,282))
print(img_cat.shape)