"""
@FileName：test_phone
@Description：
@Author：shenxinyuan
@Time：2024/9/4
"""
import re

phone_pattern = re.compile("^(?:(?:\+|00)86)?1[3-9]\d{9}$")

def is_valid_phone(phone):
    return phone_pattern.match(phone)
    # return phone_pattern.search(phone)

if __name__ == '__main__':
    print(is_valid_phone("13800138000"))
    print(is_valid_phone("008613800138000"))
    print(is_valid_phone("008913800138000"))
    print(is_valid_phone("15137482451"))
    print(is_valid_phone("021-23456789"))
