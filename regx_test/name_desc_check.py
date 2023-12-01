"""
@FileName：name_desc_check.py
@Description：
@Author：shenxinyuan
@Time：2023/11/28
"""

import re


def find_invalid_characters(input_string):
    invalid_characters = ""
    # 使用正则表达式找出不符合规则的字符
    # pattern = re.compile(r'[^\u4e00-\u9fa5a-zA-Z0-9_()\-\s]')
    pattern = re.compile(r'^[\u4e00-\u9fa5a-zA-Z0-9_()（）\-\s]+$')
    if not re.match(pattern, input_string):
        print("输入字符串不符合规则")
        # 使用正则表达式找出不符合规则的字符
        invalid_characters = re.findall(r'[^\u4e00-\u9fa5a-zA-Z0-9_()（）\-\s]', input_string)
    return invalid_characters


# 测试字符串
# test_string = "Hello_123 (测试) - World!@#"
test_string = "你 好2_-()（）"

# 找出不符合规则的字符
invalid_chars = find_invalid_characters(test_string)

# 输出结果
print("不符合规则的字符:", invalid_chars)
