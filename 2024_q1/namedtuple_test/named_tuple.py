"""
@FileName：named_tuple.py
@Description：
@Author：shenxinyuan
@Time：2024/3/25
"""
from collections import namedtuple

# 定义一个namedtuple类型User，并包含name，sex和age属性。
User = namedtuple('User', ['name', 'sex', 'age'])

# 创建一个User对象
user = User(name='Runoob', sex='male', age=12)

# 获取所有字段名
print(user._fields)

# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user = User._make(['Runoob', 'male', 12])

print(user)
# User(name='user1', sex='male', age=12)

# 获取用户的属性
print(user.name)
print(user.sex)
print(user.age)

# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print(user)
# User(name='user1', sex='male', age=21)

# 将User对象转换成字典，注意要使用"_asdict"
print(user._asdict())
# OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])