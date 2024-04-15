"""
@FileName：test_not_dataframe.py
@Description：
@Author：shenxinyuan
@Time：2024/4/10
"""
# t通过字典创建 dataframe
import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
if df:
    print(df)
