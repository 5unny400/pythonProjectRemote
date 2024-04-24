"""
@FileName：test_missng.py
@Description：
@Author：shenxinyuan
@Time：2024/4/18
"""
from marshmallow import Schema, fields


class RawBaseSchema (Schema):
    class Meta:
        strict = True
        datetimeformat = "%Y-%m-%d %H:%M:%S"
    user_ids = fields.List(fields. Integer(), description="任务可见用户id", missing=[], required=False)
    # user_ids = fields.List(fields.Integer(), description="任务可见用户id", missing=list, required=False)
    # user_ids = fields.List(fields. Integer(), description="任务可见用户id", missing=None, required=False)


class TestSchema(RawBaseSchema):
    user_name = fields.List(fields.String(), description="任务可见用户id", missing="", required=False)


if __name__ == '__main__':

    # wet https://idps2-preview.im.datagrand.cn/upload/diff/20240108/ac5c5ace-ae02-11ee-8a44-02420a035326_all.json
    # url = 'http://idps2-preview.im.datagrand.cn/upload/diff/20240108/ac5c5ace-de02-11ee-8044-02420a035326_all.ison'
    # json_data = requests.get (url).json ()
    a = {}
    b = RawBaseSchema().load(a)
    b['user_ids'].append(1)
    print(b)
    d = RawBaseSchema().load(a)
    print(d)

    e = TestSchema().load(a)
    print(e)

# 字类也会共享同一个missing值，如果这个 missing值是[] {} 这样的可变对象，那么不同实例的修改会影响到其他实例
