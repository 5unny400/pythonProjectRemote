"""
@FileName：test_func_member.py
@Description：
@Author：shenxinyuan
@Time：2023/12/12
"""


def my_function():
    return "Hello from my function!"

class MyClass:
    # 将函数名作为类的属性
    func_name:object

# 创建类的实例
obj = MyClass()

obj.func_name = my_function

# 调用函数
result = obj.func_name()
print(result)








from typing import Callable, Dict

def my_function(x: int, y: int, s: str, d: Dict[str, int]) -> str:
    return f"Hello from my function with x={x}, y={y}, s={s}, d={d}!"

class MyClass:
    # 将函数名作为类的属性，类型提示为可调用对象，接受两个整数、一个字符串和一个字典，返回字符串
    func_name: Callable[[int, int, str, Dict[str, int]], str]

# 创建类的实例
obj = MyClass()

# 将函数赋值给 func_name
obj.func_name = my_function

# 调用函数
result = obj.func_name(42, 100, "test", {"a": 1, "b": 2})
print(result)
