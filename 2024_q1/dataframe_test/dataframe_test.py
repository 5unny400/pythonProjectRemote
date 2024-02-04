"""
@FileName：dataframe_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/29
"""
import pandas as pd

# 创建一个示例 DataFrame
data = {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C': [1, 2, 3, 4, 5, 6, 7, 8]}
df = pd.DataFrame(data)

# 按照列 'A' 进行分组
grouped = df.groupby('A')

type_grouped = type(grouped)
print(type_grouped)

# 遍历分组
for group_name, group_indices in grouped.groups.items():
    # 获取每个分组的 DataFrame
    group_df = df.loc[group_indices]
    print(f"Group Name: {group_name}")
    print(group_df)
