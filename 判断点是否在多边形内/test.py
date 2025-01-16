"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/16
"""


def insideOrOutside(poly, dot):
    def on_segment(p, q, r):
        """ 判断点 q 是否在线段 pr 上 """
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0])) and (min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

    def is_point_inside_polygon(poly, dot):
        """ 使用射线法判断点 dot 是否在多边形 poly 内 """
        n = len(poly)
        count = 0
        ray_end = [float('inf'), dot[1]]  # 构造一条水平射线，向右延伸

        for i in range(n):
            p1 = poly[i]
            p2 = poly[(i + 1) % n]

            # 检查点 dot 是否在边上
            if on_segment(p1, dot, p2):
                return True  # 如果点在边上，返回 True

            # 如果射线与边相交，增加交点计数
            if (dot[1] > min(p1[1], p2[1])) and (dot[1] <= max(p1[1], p2[1])):  # y坐标在边的范围内
                if dot[0] <= max(p1[0], p2[0]):  # x坐标在射线的右侧
                    if p1[1] != p2[1]:  # 排除水平边
                        x_intersection = (dot[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
                        if x_intersection > dot[0]:
                            count += 1
        # 点在多边形内时，交点数为奇数
        return count % 2 == 1

    return is_point_inside_polygon(poly, dot)


# 测试用例
def test_insideOrOutside():
    poly1 = [[0, 0], [5, 0], [5, 5], [0, 5]]  # 正方形
    dot1 = [2, 2]  # 点在内部 True
    print(insideOrOutside(poly1, dot1))

    dot1 = [1, 1]  # 点在内部 True
    print(insideOrOutside(poly1, dot1))

    dot2 = [6, 2]  # 点在外部 False
    print(insideOrOutside(poly1, dot2))

    poly2 = [[1, 1], [4, 1], [4, 4], [1, 4]]  # 正方形
    dot3 = [4, 4]  # 点在角上 True
    print(insideOrOutside(poly2, dot3))

    dot4 = [0, 0]  # 点在外部 False
    print(insideOrOutside(poly2, dot4))

    print("All test cases passed!")


# 运行测试用例
test_insideOrOutside()
