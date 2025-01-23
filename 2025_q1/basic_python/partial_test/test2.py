"""
@FileName：test2
@Description：
@Author：shenxinyuan
@Time：2025/1/21
"""
import functools
# 当传入：

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

print(max2(5, 6, 7))
# 相当于：


args = (10, 5, 6, 7)
print(max(*args))