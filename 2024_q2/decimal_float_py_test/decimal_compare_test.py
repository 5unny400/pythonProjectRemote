"""
@FileName：decimal_compare_test.py
@Description：
@Author：shenxinyuan
@Time：2024/4/1
"""
from decimal import Decimal, getcontext

# 设置上下文精度为3位，舍入方式为四舍五入
getcontext().prec = 3
getcontext().rounding = "ROUND_HALF_UP"

a = Decimal('3.232')
b = Decimal('3.233')

# 比较操作
print(a == b)  # 输出 False
print(a != b)  # 输出 True
print(a < b)  # 输出 True
print(a > b)  # 输出 False
print(a <= b)  # 输出 True
print(a >= b)  # 输出 False