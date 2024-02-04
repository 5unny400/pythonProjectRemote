"""
@FileName：test_list_jian.py
@Description：
@Author：shenxinyuan
@Time：2024/1/29
"""
list1 = {1, 2, 3, 4, 5, 5, 5}

list2 = [4, 5]

print(list1)
print(type(list1))

res = list1 - set(list2)

print(res)
