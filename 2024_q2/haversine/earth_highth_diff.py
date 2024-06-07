import math

# 地球半径（假设为6371公里），第一次高度差1米
R = 6371 * 1000  # 单位换算成米
height_difference = 1  # 高度差1米

# 第一次绕地球的周长
C1 = 2 * math.pi * R

# 第二次绕地球的周长（高1米）
C2 = 2 * math.pi * (R + height_difference)

# 周长差异
delta_C = C2 - C1

print(f"两次绕地球一圈的周长差异为: {delta_C:.4f} 米")
