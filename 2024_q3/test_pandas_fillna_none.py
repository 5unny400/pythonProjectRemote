# 构造存在缺失值的DataFrame，并使用 replace 填充缺失值。
import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, np.nan], 'B': [4, 5, np.nan, 7], 'C': [pd.NaT, 9, 10, 11]})

print(df)

# df.replace(np.nan, None, inplace=True)
df = df.replace({np.nan: None})

print(df)
