from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # 计算从低到高第 k 个二进制位数值为 1 的元素个数
        def maxlen(k: int):
            res = 0
            for num in candidates:
                if num & (1 << k):
                    res += 1
            return res

        res = 0
        for i in range(24):
            # 遍历二进制位
            res = max(res, maxlen(i))
        return res


solution = Solution()
print(solution.largestCombination(candidates=[16, 17, 71, 62, 12, 24, 14]))

# 输入：candidates = [16,17,71,62,12,24,14]
# 输出：4
# 解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。
# 组合长度是 4 。
# 可以证明不存在按位与结果大于 0 且长度大于 4 的组合。
# 注意，符合长度最大的组合可能不止一种。
# 例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。
