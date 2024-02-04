"""
@FileName：deeepcopy_test.py
@Description：
@Author：shenxinyuan
@Time：2024/2/1
"""
import pandas as pd
import copy

# 假设 df 是你的原始 DataFrame 对象
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# 使用 deepcopy 创建 DataFrame 对象的深拷贝
df_copy = copy.deepcopy(df)

# 对 df 进行修改
df.loc[0, 'A'] = 99

# 打印两个 DataFrame 对象，观察它们的内容
print("Original DataFrame:")
print(df)

print("\nDeep Copy of DataFrame:")
print(df_copy)
