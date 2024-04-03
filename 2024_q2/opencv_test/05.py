"""
@FileName：05.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

# 导入 OpenCV 库
import cv2 as cv

img = cv.imread("./1.jpg",)
b,g,r = cv.split(img)

print(b)