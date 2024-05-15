"""
@FileName：dynamic_cal.py
@Description：这段代码使用了一个二维数组 dp 来存储中间结果，dp[i][j] 表示使用前 i 个数字构成和为 j 的所有组合。通过动态规划的方式填充这个
数组，最终得到的 dp[len(numbers)][target] 即为所有符合条件的数字组合。这种方式可以避免重复计算，提高效率。
@Author：shenxinyuan
@Time：2024/5/14
"""
import datetime


def find_combinations(numbers, target):
    dp = [[[] for _ in range(target + 1)] for _ in range(len(numbers) + 1)]
    dp[0][0] = [[]]
    for i in range(1, len(numbers) + 1):
        for j in range(target + 1):
            if j < numbers[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + [comb + [numbers[i - 1]] for comb in dp[i - 1][j - numbers[i - 1]]]
    return dp[len(numbers)][target]


# 示例
numbers = list(range(1, 21))  # 从1到100的数字
target = 59
start_time = datetime.datetime.now()
result = find_combinations(numbers, target)
end_time = datetime.datetime.now()
print(result)
print(f"Execution time: {(end_time - start_time).total_seconds()} seconds")
