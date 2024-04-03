"""
@FileName：03.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

# 导入 OpenCV 库
import cv2 as cv

img = cv.imread("./1.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()