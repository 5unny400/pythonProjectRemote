from marshmallow import Schema, fields


class A(Schema):
    test_list = fields.List(fields.String(), missing=[])


class B(Schema):
    test_list = fields.List(fields.String(), missing=lambda: [])


class C(Schema):
    test_list = fields.List(fields.String(), missing=list)


if __name__ == '__main__':
    a = A().load({})
    a['test_list'].append('1')
    b = A().load({})
    b['test_list'].append('2')
    # 定义字段时如果使用 missing=[]，会导致使用同一个的list
    print("b对象的修改更新到a中了", a['test_list'])
    print("a的ID==b的ID值：", id(a) == id(b))
    print("a的值==b的值：", a.values() == b.values())
    print("a的属性字典的id==b的属性字典的id：", id(a['test_list'] == id(b['test_list'])))

    print("======================")
    a2 = B().load({})
    a2['test_list'].append('1')
    b2 = B().load({})
    b2['test_list'].append('2')
    # lambda表达式不影响
    print(a2['test_list'])

    print("======================")
    a3 = C().load({})
    a3['test_list'].append('1')
    b3 = C().load({})
    b3['test_list'].append('2')
    # 使用list不影响，表达式不影响
    print(a3['test_list'])
