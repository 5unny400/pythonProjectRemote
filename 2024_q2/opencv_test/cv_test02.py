"""
@FileName：cv_test02.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

# 导入 OpenCV 库
import cv2 as cv

# 灰色显示
img = cv.imread("./1.jpg",cv.IMREAD_GRAYSCALE)

# 打印信息
print(img)