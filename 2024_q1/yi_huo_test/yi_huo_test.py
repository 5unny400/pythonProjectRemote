"""
@FileName：yi_huo_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/22
"""
# 异或方法
def are_numbers_equal(a, b):
    return a ^ b == 0

# 示例
num1 = 5
num2 = 5
num3 = 8

result1 = are_numbers_equal(num1, num2)  # 返回 True，因为5和5相等
print(result1)
result2 = are_numbers_equal(num1, num3)  # 返回 False，因为5和8不相等
print(result2)


# 同或方法
def xnor(a, b):
    return (a & b) | (~a & ~b)

# 例子
num1 = 5
num2 = 5

result = xnor(num1, num2)

if result:
    print("两个数相等")
else:
    print("两个数不相等")
