"""
@FileName：json_methods_together.py
@Description：
@Author：shenxinyuan
@Time：2023/12/13
"""
from functools import wraps
import operator
from typing import Any, Callable


def filter_by_column(column_index: int, json_key: str, condition: Callable[[Any], bool]):
    """
    装饰器：根据指定列和条件筛选数据。

    :param column_index: 需要筛选的列的索引。
    :param json_key: 如果列是JSON，这是JSON对象内的键的路径，用'.'分隔。
    :param condition: 一个函数，接受列的值作为输入，返回布尔值。
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 执行原始函数
            result = func(*args, **kwargs)

            # 筛选数据
            filtered_data = []
            for row in result:
                column_value = row[column_index]

                # 如果是JSON，获取特定键的值
                if json_key:
                    for key in json_key.split('.'):
                        column_value = column_value.get(key, None)
                        if column_value is None:
                            break

                # 应用条件
                if condition(column_value):
                    filtered_data.append(row)

            return filtered_data

        return wrapper

    return decorator


# 示例用法
@filter_by_column(column_index=3, json_key="status", condition=lambda x: x != "success")
def get_data():
    # 这里是模拟的数据库查询结果
    return [
        (1, "apple", "多列值", {"status": "processing"}),
        (2, "blue", "多列值", {"status": "success"}),
        (3, "yellow", "多列值", {"status": "processing"}),
    ]


# 测试装饰器
print(get_data())