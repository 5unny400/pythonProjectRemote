"""
@FileName：sorted_test.py
@Description：
@Author：shenxinyuan
@Time：2024/3/7
"""
import random
import time

# 生成随机数据
data = [random.randint(1, 100_0000) for _ in range(40_0000)]

# 记录开始排序前的时间
start_time = time.time()

# 对数据进行排序
sorted_data = sorted(data)

# 记录排序结束后的时间
end_time = time.time()

# 输出排序所花费的时间
print("Sorting took", end_time - start_time, "seconds.")
