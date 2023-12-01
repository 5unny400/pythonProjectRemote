"""
@FileName：list_index.py
@Description：
@Author：shenxinyuan
@Time：2023/12/1
"""

# 在 Python 中，list 类型提供了 index 方法，用于查找指定元素在列表中的索引位置。index 方法的基本语法如下：

# list.index(element, start, end)
# element：要查找的元素。
# start：可选参数，指定开始查找的索引位置，默认为 0。
# end：可选参数，指定结束查找的索引位置，默认为列表的长度。
# 如果找到指定元素，index 方法返回该元素在列表中的第一个匹配项的索引；如果未找到，会引发 ValueError 异常。

my_list = [1, 2, 3, 4, 3, 5]

# 查找元素 3 的索引
index_of_3 = my_list.index(3)
print(f"Index of 3: {index_of_3}")

# 查找元素 3 的索引，从索引 2 开始搜索
index_of_3_starting_from_2 = my_list.index(3, 2)
print(f"Index of 3 starting from index 2: {index_of_3_starting_from_2}")

# 查找元素 6 的索引，如果未找到会引发 ValueError
try:
    index_of_6 = my_list.index(6)
except ValueError as e:
    print(f"ValueError: {e}")
