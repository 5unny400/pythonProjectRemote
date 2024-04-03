"""
@FileName：decimal_test.py
@Description：
@Author：shenxinyuan
@Time：2024/4/1
"""
# 使用 Decimal 类型进行计算
from decimal import Decimal

total_float = 0.1 + 0.2
total_decimal = Decimal('0.1') + Decimal('0.2')
print("[0.1 + 0.2] 使用 float 类型进行计算：", total_float)  # 输出可能是 0.30000000000000004，而不是期望的 0.3
print("[0.1 + 0.2] 使用 Decimal 类型进行计算：", total_decimal)
print()
print("[1.23 ÷ 0.1] 使用 float 类型进行计算：", (1.23 / 0.1))  # 输出可能是 12.299999999999999 而不是期望的 12.3
print("[1.23 ÷ 0.1] 使用 Decimal 类型进行计算：", Decimal('1.23') / Decimal('0.1'))
print("[1.23 ÷ 0.1] 使用 float ->转成-> Decimal 类型进行计算：", Decimal(1.23) / Decimal(0.1))
print()
print("[1.23 + 0.1] 使用 float 类型进行计算：", (1.23 + 0.1))  # 这个可以正常输出1.33,
print("[1.23 + 0.1] 使用 Decimal 类型进行计算：", (Decimal('1.23') + Decimal('0.1')))







from decimal import Decimal

# 小数位数作为变量
decimal_places = 2

exp = Decimal('0.1') ** decimal_places

# 创建要量化的 Decimal 对象
decimal_object = Decimal('3.14159')

# 根据变量的值动态设置量化精度
quantized_result = decimal_object.quantize(exp)

print(quantized_result)  # 输出: 3.14




