"""
@FileName：test_n_num_sum.py
@Description： N 数之和
@Author：shenxinyuan
@Time：2024/5/14
"""
import datetime


def find_combinations(numbers, target, prefix=[], result=[]):
    s = sum(prefix)
    if s == target:
        result.append(prefix)
        return
    if s > target:
        return
    for i, num in enumerate(numbers):
        find_combinations(numbers[i + 1:], target, prefix + [num], result)
    return result


# 示例
numbers = list(range(1, 21))  # 从1到100的数字
target = 59
start_time = datetime.datetime.now()
result = find_combinations(numbers, target)
end_time = datetime.datetime.now()
print(result)
print(f"Execution time: {(end_time - start_time).total_seconds()} seconds")

