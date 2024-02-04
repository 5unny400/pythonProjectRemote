"""
@FileName：partial_test.py
@Description：简单翻译：partial() 是被用作 “冻结” 某些函数的参数或者关键字参数，同时会生成一个带有新标签的对象(即返回一个新的函数)。
@Author：shenxinyuan
@Time：2024/1/16
"""
from functools import partial

# 定义一个普通的函数
def multiply(x, y):
    return x * y

# 创建一个部分应用的函数，固定其中一个参数为 2
double = partial(multiply, 2)

# 调用部分应用的函数
result = double(5)
print(result)  # 输出: 10
