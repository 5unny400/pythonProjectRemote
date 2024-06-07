import time

import math


def lat_lon_to_xyz(lat, lon):
    R = 6367000  # 地球半径，单位：米
    x = R * math.cos(lat) * math.cos(lon)
    y = R * math.cos(lat) * math.sin(lon)
    z = R * math.sin(lat)
    return x, y, z


def calculate_angle(x1, y1, z1, x2, y2, z2):
    dot_product = x1 * x2 + y1 * y2 + z1 * z2
    magnitude1 = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    magnitude2 = math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)
    cos_angle = dot_product / (magnitude1 * magnitude2)
    return math.acos(cos_angle)


def calculate_distance(lat1, lon1, lat2, lon2):
    x1, y1, z1 = lat_lon_to_xyz(lat1, lon1)
    x2, y2, z2 = lat_lon_to_xyz(lat2, lon2)
    angle = calculate_angle(x1, y1, z1, x2, y2, z2)
    distance = angle * 6367000  # 将弧度转换为米
    return distance


# 测试数据
points = [
    # (39.941, 116.45, 39.94, 116.451),  # 接近的点对
    # (39.96, 116.45, 39.94, 116.40),  # 千米级别的点对
    # (39.96, 116.45, 39.94, 117.30),  # 较远距离的点对
    (40.0, 116.0, 91.0, 29.0)    # 北京-拉萨
]

# 计算并打印距离
for point in points:
    lat1, lon1, lat2, lon2 = point
    time_start = time.time()
    for i in range(100_0000):
        distance = calculate_distance(lat1, lon1, lat2, lon2)
    time_end = time.time()
    print(f"计算一百万次Time used: {time_end - time_start} seconds")
    print(f"Distance between ({lat1}, {lon1}) and ({lat2}, {lon2}) is {distance/1000:.2f} kilometers")
