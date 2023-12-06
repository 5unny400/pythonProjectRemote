"""
@FileName：args_kwargs_test.py
@Description：*args：表示接受任意数量的位置参数。
**kwargs：表示接受任意数量的关键字参数
@Author：shenxinyuan
@Time：2023/12/6
"""


def example_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


example_function(1, 2, 3, name="John", age=25)
# 输出:
# 1
# 2
# 3
# name: John
# age: 25
