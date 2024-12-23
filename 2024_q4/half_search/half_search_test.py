"""
@FileName：half_search_test
@Description：
@Author：shenxinyuan
@Time：2024/12/16
"""


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # 计算中间元素的下标

        if arr[mid] == target:
            return mid  # 找到目标元素，返回其下标
        elif arr[mid] < target:
            low = mid + 1  # 目标元素在右半部分
        else:
            high = mid - 1  # 目标元素在左半部分

    return -1  # 如果没有找到目标元素，返回 -1


# 示例：在有序数组中查找目标元素
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"目标元素 {target} 的下标是 {result}")
else:
    print(f"目标元素 {target} 未找到")
