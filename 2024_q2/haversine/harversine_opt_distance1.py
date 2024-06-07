import time

import math


def distance_simplify(lat1, lng1, lat2, lng2):
    dx = lng1 - lng2  # 经度差值
    dy = lat1 - lat2  # 纬度差值
    b = (lat1 + lat2) / 2.0  # 平均纬度
    Lx = math.radians(dx) * 6367000.0 * math.cos(math.radians(b))  # 东西距离
    Ly = 6367000.0 * math.radians(dy)  # 南北距离
    return math.sqrt(Lx * Lx + Ly * Ly)  # 用平面的矩形对角距离公式计算总距离


# 示例调用
# lat1 = 30.658601
# lng1 = 104.064856
# lat2 = 31.230391
# lng2 = 121.473701
# lng1, lat1 = -73.9857, 40.7488  # 点1的经纬度（如纽约帝国大厦）
# lng2, lat2 = 139.6917, 35.6895  # 点2的经纬度（如东京塔）
# lat1, lng1 = 40.7128, -74.0060
# lat2, lng2 = 34.0522, -118.2437
lat1, lng1 = 40.0, 116.0    # 北京
lat2, lng2 = 91.0, 29.0     # 拉萨
time_start = time.time()
for i in range(100_0000):
    distance = distance_simplify(lat1, lng1, lat2, lng2)
time_end = time.time()
print(f"计算一百万次Time cost: {time_end - time_start} seconds")
print(f"距离简化计算Distance: {distance/1000:.2f} kilometers")
