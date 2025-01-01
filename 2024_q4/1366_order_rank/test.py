import collections


class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        n = len(votes[0])
        # 初始化哈希映射
        ranking = collections.defaultdict(lambda: [0] * n)
        # 遍历统计
        for vote in votes:
            for i, vid in enumerate(vote):
                ranking[vid][i] += 1

        # 取出所有的键值对
        result = list(ranking.items())
        # 排序
        result.sort(key=lambda x: (x[1], -ord(x[0])), reverse=True)
        # 将 vid 从字符转换为对应的 ASCII 码，并用其相反数作为第二关键字，这样就与第一关键字保持一致，即都进行降序排序。
        return "".join([vid for vid, rank in result])


solution = Solution()
votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
print(solution.rankTeams(votes))


# 输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
# 输出："ACB"
# 解释：
# A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
# B 队获得两票「排位第二」，三票「排位第三」。
# C 队获得三票「排位第二」，两票「排位第三」。
# 由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。
