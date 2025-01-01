class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join([bin(int(num))[2:] for num in date.split('-')])

    