from functools import wraps
from collections import defaultdict

def aggregate_by_columns(key_columns, agg_columns):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # 聚合数据存储
            aggregated_data = defaultdict(lambda: [tuple(), *([] for _ in agg_columns), []])

            for row in result:
                # 构建聚合键和聚合值
                key = tuple(row[i] for i in key_columns)
                values = [row[i] for i in agg_columns]

                if not aggregated_data[key][0]:
                    aggregated_data[key][0] = key

                for i, value in enumerate(values):
                    aggregated_data[key][i + 1].append(value)

                # 处理非聚合列
                non_agg_columns = [row[i] for i in range(len(row)) if i not in agg_columns + key_columns]
                aggregated_data[key][-1] = non_agg_columns

            # 构建最终结果
            aggregated_result = []
            for key, values in aggregated_data.items():
                row_data = list(values[0])
                for agg_value in values[1:-1]:
                    row_data.append(agg_value)
                row_data.extend(values[-1])  # 添加非聚合列的数据
                aggregated_result.append(tuple(row_data))

            return aggregated_result

        return wrapper
    return decorator

# 示例用法
@aggregate_by_columns([0], [1])
def get_data():
    # 这里是模拟的数据库查询结果
    return [
        (1, "apple", "多列值"),
        (2, "blue", "多列值"),
        (3, "yellow", "多列值"),
        (1, "people", "多列值")
    ]

# 测试装饰器
print(get_data())