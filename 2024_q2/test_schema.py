from datetime import datetime

from marshmallow import Schema, fields, EXCLUDE
from numpy import nan
from pandas import NaT


class RawBaseSchema(Schema):
    class Meta:
        strict = True
        datetimeformat = "%Y-%m-%d %H:%M:%S"
        unknown = EXCLUDE


# 示例使用
class ExampleSchema(RawBaseSchema):
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    error_time = fields.DateTime()


# 创建一个示例数据
example_data = {
    "created_at": None,      # 直接返回 None 不会再 strftime
    "updated_at": datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
    # "error_time": "",     # 'str' object has no attribute 'strftime'
    # "error_time": NaT,    # NaTType does not support strftime
    # "error_time": nan,      # 'float' object has no attribute 'strftime'

}

# 尝试序列化数据
try:
    result = ExampleSchema().dump(example_data)
    print(result)  # 输出: {'created_at': ''}
except Exception as e:
    print(e)
