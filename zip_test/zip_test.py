"""
@FileName：zip_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/7
"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']  # 使用zip函数将两个列表打包成元组的迭代器
zipped = zip(list1, list2)  # 将迭代器转换为列表
result_list = list(zipped)

print(result_list)



unsorted_tuple = tuple([list1, list2])
for e in unsorted_tuple:
    print(e)