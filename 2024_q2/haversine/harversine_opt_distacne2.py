import time

import numpy as np
from scipy.optimize import curve_fit
import math


# 定义多项式拟合函数
def poly_fit_func(x, *coeffs):
    return sum(c * x ** i for i, c in enumerate(reversed(coeffs)))


# 训练多项式拟合
def train_poly_fit(degree, length):
    min_lat = 10.0  # 中国最低纬度
    max_lat = 60.0  # 中国最高纬度
    interv = (max_lat - min_lat) / length
    x_data = np.array([min_lat + i * interv for i in range(length)])
    y_data = np.cos(np.radians(x_data))

    # 使用 curve_fit 进行多项式拟合
    coeffs, _ = curve_fit(f=poly_fit_func, xdata=x_data, ydata=y_data, p0=[1] * (degree + 1))
    return coeffs


# 计算两个地理坐标之间的距离
def distance_simplify_more(lat1, lng1, lat2, lng2, coeffs):
    dx = lng1 - lng2  # 经度差值
    dy = lat1 - lat2  # 纬度差值
    b = (lat1 + lat2) / 2.0  # 平均纬度

    # 计算东西距离
    Lx = sum(c * b ** i for i, c in enumerate(reversed(coeffs))) * math.radians(dx) * 6367000.0
    # 计算南北距离
    Ly = 6367000.0 * math.radians(dy)

    # 计算总距离
    return math.sqrt(Lx * Lx + Ly * Ly)


# 示例调用
degree = 3
length = 100

# 生成拟合多项式系数
coeffs = train_poly_fit(degree, length)
print("拟合多项式系数:", coeffs)

# 测试数据
# lat1 = 30.658601
# lng1 = 104.064856
# lat2 = 31.230391
# lng2 = 121.473701
lat1, lng1 = 40.0, 116.0    # 北京
lat2, lng2 = 91.0, 29.0     # 拉萨

# 计算距离
time_start = time.time()
for i in range(100_0000):
    distance = distance_simplify_more(lat1, lng1, lat2, lng2, coeffs)
time_end = time.time()
print(f"计算一百万次耗时: {time_end - time_start} 秒")
print(f"两个地理坐标之间的距离: {distance/1000.0:.2f} 公里")
