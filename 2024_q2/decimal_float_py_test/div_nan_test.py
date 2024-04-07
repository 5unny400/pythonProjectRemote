"""
@FileName：div_nan_test.py
@Description：
@Author：shenxinyuan
@Time：2024/4/7
"""
import pandas as pd
from decimal import Decimal

# 创建包含 NaN 的 DataFrame
data = {
    "numerator": [1.0, 2.0, 3.0, 4.0],
    "denominator": [2.0, float("nan"), 4.0, 0.0]
}
df = pd.DataFrame(data)

# 使用浮点数进行除法计算
df["result_float"] = df["numerator"] / df["denominator"]
print("使用浮点数计算结果:")
print(df["result_float"])

# 使用 Decimal 类型进行除法计算
df["result_decimal"] = df["numerator"].apply(Decimal) / df["denominator"].apply(Decimal)
print("使用 Decimal 计算结果:")
print(df["result_decimal"])


