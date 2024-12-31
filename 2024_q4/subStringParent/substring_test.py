"""
@FileName：substring_test
@Description：
@Author：shenxinyuan
@Time：2024/12/26
"""
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i+2][::-1] in s:
                return True
        return False


if __name__ == '__main__':
    s = "abcabc"
    print(Solution().isSubstringPresent(s))
