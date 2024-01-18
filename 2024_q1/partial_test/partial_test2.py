"""
@FileName：partial_test2.py
@Description：
@Author：shenxinyuan
@Time：2024/1/16
"""
from functools import partial

# 定义一个函数
def power(base, exponent):
    return base ** exponent

# 使用 partial 固定其中一个参数
square = partial(power, exponent=2)

# 调用部分应用的函数
result = square(5)
print(result)  # 输出: 25
