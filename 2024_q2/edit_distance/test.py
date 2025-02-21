"""
@FileName：翻转二维数组.py
@Description：编辑距离算法
@Author：shenxinyuan
@Time：2024/4/26
"""


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


# Example usage
s1 = "kitten"
s2 = "sitting"
# 编辑距离越短，说明两个字符串越相似
print("编辑距离：" + str(edit_distance(s1, s2)))  # Output: 3
