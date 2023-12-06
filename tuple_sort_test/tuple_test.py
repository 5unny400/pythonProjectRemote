"""
@FileName：tuple_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/6
"""
unsorted_tuple = ((3, 2, 5), (1, 4, 6), (2, 3, 1))

# 如果第一个值相同的时候才按照第二个元素排序
# sorted_tuple = tuple(zip(*sorted(zip(*unsorted_tuple), key=lambda x: (x[0], x[1]))))

sorted_tuple = tuple(sorted(unsorted_tuple, key=lambda x: (x[0], x[1])))

print(sorted_tuple)
