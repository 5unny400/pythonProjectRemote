
# 一个转换二维数组的行和列的python函数

# 方式一
def transpose(two_dimesion_list):
    return [list(i) for i in zip(*two_dimesion_list)]

list1 = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
]

print(transpose(list1))

