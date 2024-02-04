"""
@FileName：test_int32_int.py
@Description：
@Author：shenxinyuan
@Time：2024/1/31
"""
import numpy as np

# 创建一个包含大量整数的 NumPy 数组
arr_int = np.arange(100_0000, dtype=int)
arr_int32 = np.arange(100_0000, dtype=np.int32)

# 比较内存使用
memory_usage_int = arr_int.nbytes / (1024 ** 2)  # 单位：MB
memory_usage_int32 = arr_int32.nbytes / (1024 ** 2)  # 单位：MB

print(f"Memory usage with int: {memory_usage_int:.2f} MB")
print(f"Memory usage with int32: {memory_usage_int32:.2f} MB")
