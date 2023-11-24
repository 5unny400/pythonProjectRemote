"""
@FileName：regx.py
@Description：
@Author：shenxinyuan
@Time：2023/11/23
"""
import re

expression = input("输入要匹配的字符串:")
# [[完税证明_填票人]]
# [[完税证明|填票人]]
# ##完税证明|填票人|奥阿唯粉还加班呢##
# ##完税证明|填票人##
# ##合同金额审核|合同总金额（含税）（小写）##
# ##组合字段22|一句话|时间##

regex = r"\#\#(((?!\[|\]).)*)\#\#"  # [[x文档_x字段]]的格式
re_result = list(re.finditer(regex, expression))
for i in range(len(re_result) - 1, -1, -1):
    res = re_result[i]
    start, end, match = res.start(1), res.end(1), res.group(1)
    name_list = match.split("|")
    print(name_list)
