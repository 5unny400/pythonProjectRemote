import time

import math


def haversine(lon1, lat1, lon2, lat2):
    # 将度数转换为弧度
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    r = 6371  # 地球半径，单位为公里
    return c * r


# 示例
# lon1, lat1 = -73.9857, 40.7488  # 点1的经纬度（如纽约帝国大厦）
# lon2, lat2 = 139.6917, 35.6895  # 点2的经纬度（如东京塔）

# lat1, lon1 = 40.7128, -74.0060
# lat2, lon2 = 34.0522, -118.2437
lat1, lon1 = 40.0, 116.0    # 北京
lat2, lon2 = 91.0, 29.0     # 拉萨
time_start = time.time()
for i in range(100_0000):
    distance = haversine(lon1, lat1, lon2, lat2)
time_end = time.time()
print(f"用时: {time_end - time_start:.4f} 秒")
print(f"哈维斯计算两个点之间的距离是: {distance:.2f} 公里")
