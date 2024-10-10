"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/9/24
"""
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


print(get_distance_simplify(39.912887, 116.466275, 39.912887, 116.466275))
