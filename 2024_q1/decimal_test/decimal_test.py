"""
@FileName：decimal_test.py
@Description：
@Author：shenxinyuan
@Time：2024/2/5
"""
from decimal import Decimal, getcontext

# 设置精度上下文，这里设置小数点后5位
getcontext().prec = 5

# 使用Decimal进行高精度计算
result = Decimal('1.23456789') + Decimal('2.34567890')

print(result)  # 输出: 3.5802
