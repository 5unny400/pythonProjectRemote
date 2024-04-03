"""
@FileName：10merge01.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

import cv2 as cv

img = cv.imread("./1.jpg")
img_cat = cv.imread("./2.jpg")

print(img.shape)
print(img_cat.shape)
