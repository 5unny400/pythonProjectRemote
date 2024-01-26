"""
@FileName：time_delta_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/26
"""
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()

# 创建一个 timedelta 对象，表示一天的时间间隔
one_day = timedelta(days=1)

# 计算昨天的日期
yesterday = now - one_day

# 输出结果
print("当前时间:", now)
print("昨天的时间:", yesterday)
