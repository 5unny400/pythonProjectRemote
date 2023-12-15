"""
@FileName：test_func2.py
@Description：
@Author：shenxinyuan
@Time：2023/12/12
"""
import types

class MyClass:
    pass

# 定义一个随机的方法
def my_random_method(self,something):
    return f"{something}_Hello from my random method!"

# 创建类的实例
obj = MyClass()

# 将方法绑定到实例
obj.my_method = types.MethodType(my_random_method, obj)

# 调用方法
result = obj.my_method("we ")
print(result)
