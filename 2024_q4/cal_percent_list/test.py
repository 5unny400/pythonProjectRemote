
"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/11/18
"""
from typing import List


def _calculate_percent(percent_list: List[str]):
    """
    计算占股比
    """
    if not percent_list:
        return "(占股比未知)"

    # 过滤掉空字符串和无效值
    valid_percent_list = []
    for percent in percent_list:
        percent = percent.strip().strip("%")  # 去掉空白和百分号
        if percent:  # 确保不是空字符串
            try:
                valid_percent_list.append(float(percent))
            except ValueError:
                pass  # 忽略无法转换的值

    if not valid_percent_list:  # 如果没有有效的值
        return "(占股比未知)"

    if len(valid_percent_list) == 1:
        return f"{valid_percent_list[0]}%"
    else:
        return f"{sum(valid_percent_list) / len(valid_percent_list):.4f}%"


percent_list = ["10.57888%", "20.3%", "30.2%", ""]
print(_calculate_percent(percent_list))
