"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/9/4
"""

content = ["", "-", 0, 1, False, True, None, [], {}, set()]    # not String


for x in content:
    # print(not x)
    print("not "+str(x)+":  " + str(not x))
