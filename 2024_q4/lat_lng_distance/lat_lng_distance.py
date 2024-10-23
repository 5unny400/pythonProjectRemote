"""
@FileName：lat_lng_distance
@Description：
@Author：shenxinyuan
@Time：2024/10/18
"""
import math


def distHaversineRAD(lat1, lon1, lat2, lon2):
    hsinX = math.sin((lon1 - lon2) * 0.5)
    hsinY = math.sin((lat1 - lat2) * 0.5)
    h = (hsinY * hsinY + (math.cos(lat1) * math.cos(lat2) * hsinX * hsinX))
    return 2 * math.atan2(math.sqrt(h), math.sqrt(1 - h)) * 6367000


from math import radians, cos, sqrt

r = 6367000.0  # 半径


def get_distance_simplify(lat_a, lon_a, lat_b, lon_b):
    """
    允许一定误差下，根据两个点的经纬度计算两点距离
    @param:lon_a a点经度
    @param:lat_a a点纬度
    @param:lon_b b点经度
    @param:lat_b b点纬度
    原理：
    1.纬线的长度是赤道的周长乘以纬线的纬度的余弦
    2.弧线长度=r*夹角度(弧度制)
    3.假定两个坐标的经线和纬线相互垂直
    4.南北方向ly = R*纬度差*Math.PI/180.0；
    5.东西方向lx = R*经度差*Cos<当地纬度数* Math.PI/180.0>
    """
    # change angle to radians
    # r = 6367000.0  # 半径
    dx = lon_a - lon_b  # 经度差值
    dy = lat_a - lat_b  # 纬度差值
    b = (lat_a + lat_b) / 2.0  # 平均纬度
    lx = radians(dx) * r * cos(radians(b))  # 东西距离
    ly = r * radians(dy)  # 南北距离
    return sqrt(lx * lx + ly * ly)  # 用平面的矩形对角距离公式计算总距离

def haversine(lat1, lon1, lat2, lon2):
    # 地球半径 (公里)
    R = 6371.0

    # 转换成弧度
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # 计算差值
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # 哈弗辛公式
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 计算距离
    distance = R * c
    return distance

# lat1 = 39.9042
# lon1 = 116.4074
# lat2 = 39.9063
# lon2 = 116.4038
# distance = distHaversineRAD(lat1, lon1, lat2, lon2)
# print(f"Haversine distance: {distance:.2f} m")
# distance = get_distance_simplify(lat1, lon1, lat2, lon2)
# print(f"Simplified distance: {distance:.2f} m")

lat1 = 39.9047
lon1 = 116.4074
lat2 = 39.9047
lon2 = 116.4074
distance = get_distance_simplify(lat1, lon1, lat2, lon2)
print(f"小数点后第四位的计算精度：Simplified distance: {distance:.2f} m")
distance = haversine(lat1, lon1, lat2, lon2)
print(f"小数点后第四位的计算精度：haversine distance: {distance:.2f} m")

#结论：经纬度小数点后四位相同就认为是一个地址

'''
地址: 安徽省蚌埠市怀远县榴城镇卞和路339号   经纬度: {'lng': 117.20521691771705, 'lat': 32.98841542088895}
地址:安徽省怀远县榴城镇卞和路339号         经纬度: {'lng': 117.20728948818967, 'lat': 32.97483808305965}
'''
lat1 = 32.98841542088895
lon1 = 117.20521691771705
lat2 = 32.97483808305965
lon2 = 117.20728948818967
distance = get_distance_simplify(lat1, lon1, lat2, lon2)
print(f"Simplified distance: {distance:.2f} m")

'''
地址:上海市青浦区朱家角工业园区康园路380号 经纬度: {'lng': 121.064819419319, 'lat': 31.09249666202696}
地址:上海市青浦区朱家角工业园区康园路380号中广核俊尔(上海）新材料有限公司 经纬度: {'lng': 121.06525087545545, 'lat': 31.09183380854076}
'''
lat1 = 31.09249666202696
lon1 = 121.064819419319
lat2 = 31.09183380854076
lon2 = 121.06525087545545
distance = get_distance_simplify(lat1, lon1, lat2, lon2)
print(f"Simplified distance: {distance:.2f} m")
