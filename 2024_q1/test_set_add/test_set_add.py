"""
@FileName：test_set_add.py
@Description：
@Author：shenxinyuan
@Time：2024/1/30
"""
set1 = set()
set2 = {3, 4, 5}

# 使用 update 方法将 set2 的元素添加到 set1 中
# set1 = set1.union(set2)
set1.update(set2)

print(set1)
