class Solution:
    def binary(self, x: int) -> str:
        return bin(x)[2:]

    def convertDateToBinary(self, date: str) -> str:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        return self.binary(year) + '-' + self.binary(month) + '-' + self.binary(day)


if __name__ == "__main__":
    s = Solution()
    date = "2017-05-01"
    print(s.convertDateToBinary(date))
