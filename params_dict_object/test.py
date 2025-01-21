"""
@FileName：div_zero_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/11
"""
class MyClass:
    def __init__(self, value):
        self.value = value
        self.length = len(value)

def my_function(my_dict):
    # 在函数中通过 . 引用对象的属性
    print(my_dict['obj'].value)

# 创建对象
my_object = MyClass(value=42)

# 将对象的属性添加到字典中
my_dict = {'obj': my_object}

# 调用函数，将字典作为参数传递
my_function(my_dict)
