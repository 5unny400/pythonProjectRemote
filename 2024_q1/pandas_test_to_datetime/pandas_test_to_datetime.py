"""
@FileName：pandas_test_to_datetime.py
@Description：
@Author：shenxinyuan
@Time：2024/1/30
"""
import pandas as pd

df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', 'invalid_date']})

# 日期转换错误处理方式一 会引发 ValueError: ('Unknown string format:', 'invalid_date')
pd.to_datetime(df['date'], errors='raise')

df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', 'invalid_date']})

# 日期转换错误处理方式二 转换时将 'invalid_date' 替换为 NaT，不引发异常
pd.to_datetime(df['date'], errors='coerce')

df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', 'invalid_date']})

# 日期转换错误处理方式三 转换时忽略 'invalid_date'，保留原始数据
pd.to_datetime(df['date'], errors='ignore')