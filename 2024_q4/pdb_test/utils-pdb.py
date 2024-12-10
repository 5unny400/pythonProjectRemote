"""
@FileName：utils
@Description：      python3 -m pdb utils.py
@Author：shenxinyuan
@Time：2024/11/21
"""
import pdb
pdb.set_trace()


def sum(mylist):
    result = 0
    for item in mylist:
        result += item
    return result
