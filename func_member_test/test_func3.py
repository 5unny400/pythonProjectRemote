"""
@FileName：test_func3.py
@Description：
@Author：shenxinyuan
@Time：2023/12/12
"""
class MyClass:
    # 定义一个函数
    def my_function(self):
        return "Hello from my function!"

# 创建类的实例
obj = MyClass()

# 将函数名作为类的属性
obj.my_method = MyClass.my_function

# 调用函数
result = obj.my_method(obj)
print(result)
