"""
@FileName：to_days_test.py
@Description：
@Author：shenxinyuan
@Time：2024/3/25
"""
import pandas as pd

# 示例数据
data = {'trade_date': ['1999-01-01 00:00:00', '2099-01-02 00:00:00', '2024-01-03 00:00:00']}
df = pd.DataFrame(data)

# 转换为Datetime类型
df['trade_date'] = pd.to_datetime(df['trade_date'])

# 计算日期差
# epoch = pd.Timestamp('2000-01-01')
epoch = pd.Timestamp('1970-01-01')
df['trade_date_days'] = (df['trade_date'] - epoch).dt.days

# 假设 df 是包含 trade_date 列的 DataFrame
# 计算 trade_date 列中的日期与 0000-00-00 之间的天数差
# df["trade_date_days"] = (df["trade_date"] - pd.NaT) / pd.Timedelta(days=1)
print(df)
