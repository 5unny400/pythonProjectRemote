"""
@FileName：test_empty
@Description：
@Author：shenxinyuan
@Time：2024/10/29
"""
# test_string = None
test_string = ""
if test_string:
    print(f"if test_string: {test_string}")
if not test_string:
    print(f"if not test_string: {test_string}")


test_string2 = "   "
if test_string2:
    print(f"if test_string2: {test_string2}")
if test_string2.strip():
    print(f"if test_string2.strip(): {test_string2}")
if not test_string2.strip():
    print(f"if not test_string2.strip(): {test_string2}")