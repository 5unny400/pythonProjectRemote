"""
@FileName：yi_huo_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/22
"""
def are_numbers_equal(a, b):
    return a ^ b == 0

# 示例
num1 = 5
num2 = 5
num3 = 8

result1 = are_numbers_equal(num1, num2)  # 返回 True，因为5和5相等
result2 = are_numbers_equal(num1, num3)  # 返回 False，因为5和8不相等
