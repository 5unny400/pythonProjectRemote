"""
@FileName：08blue.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

# 导入 OpenCV 库
import cv2 as cv

img = cv.imread("./1.jpg",)
cur_img = img.copy()
# 注意参数的变化
cur_img[:,:,1] = 0
cur_img[:,:,2] = 0
cv.imshow('B',cur_img)
cv.waitKey(0)
cv.destroyAllWindows()