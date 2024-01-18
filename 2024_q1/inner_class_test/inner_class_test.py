"""
@FileName：inner_class_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/17
"""
def create_person_class(name):
    class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, my name is {self.name}"

    return Person

# 在函数内声明的类仅在函数内可见
john_class = create_person_class("John")
john_instance = john_class("John Doe")
print(john_instance.greet())