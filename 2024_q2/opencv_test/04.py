"""
@FileName：04.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""

# 导入 OpenCV 库
import cv2 as cv
# 加载图像
img = cv.imread("./2.jpg",)
# 截取部分图像
cat = img[0:200, 0:200]
# 显示截取的图像
cv.imshow("cat",cat)
cv.waitKey(0)
cv.destroyAllWindows()