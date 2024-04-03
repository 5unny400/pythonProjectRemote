"""
@FileName：cv_test01.py
@Description：
@Author：shenxinyuan
@Time：2024/4/2
"""
# 导入 OpenCV 库
import cv2 as cv

# 加载图像
img = cv.imread("./1.jpg")

# 图像的显示，也可以创建多个窗口
cv.imshow("image",img)

# 等待时间，毫秒级，0 表示任意键终止
cv.waitKey(0)
cv.destroyAllWindows()