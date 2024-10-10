"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/8/27
"""
import re


class SendBankAuditService:
    def __init__(self):
        self.rural_bank_pattern = re.compile("农商行|村|镇")

    def matches_rural_bank(self, text):
        return bool(self.rural_bank_pattern.search(text))

# 测试方法
def test_rural_bank_pattern():
    service = SendBankAuditService()
    test_data = [
        ("农商行", True),
        ("村", True),
        ("镇", True),
        ("这是一个农商行", True),
        ("这是一个村", True),
        ("这是一个镇", True),
        ("农商行在这里", True),
        ("村在这里", True),
        ("镇在这里", True),
        ("城市", False),
        ("银行", False),
        ("农村", True),
        ("城镇", True),
        ("农商", False),
        ("村庄", True),
        ("镇子", True),
    ]

    for text, expected in test_data:
        result = service.matches_rural_bank(text)
        assert result == expected, f"Failed for text: '{text}'. Expected: {expected}, Got: {result}"

    print("All tests passed!")

# 运行测试
test_rural_bank_pattern()

