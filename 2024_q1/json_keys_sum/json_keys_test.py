"""
@FileName：json_keys_test.py
@Description：
@Author：shenxinyuan
@Time：2024/3/27
"""
import pandas as pd

data = {'json_col': [{'key1': 'value1', 'key2': 'value2'},
                     {'key1': 'value3', 'key2': 'value4', 'key3': 'value5'},
                     {'key2': 'value6', 'key3': 'value7'}]}
df = pd.DataFrame(data)

# 使用 transform(len) 计算每行 JSON 数据中键的总个数
df['total_keys'] = df['json_col'].transform(len)

print(df)
