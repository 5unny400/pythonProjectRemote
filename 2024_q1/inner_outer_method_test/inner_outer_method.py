"""
@FileName：inner_outer_method.py
@Description：
@Author：shenxinyuan
@Time：2024/1/16
"""
class MyClass:
    def outer_method(self):
        print("This is the outer method")

        def inner_method1():
            print("This is inner method 1")

        def inner_method2():
            print("This is inner method 2")

        # 调用内部方法
        inner_method1()
        inner_method2()

# 创建 MyClass 的实例
my_instance = MyClass()

# 调用外部方法，它会在内部调用两个内部方法 也就是内部方法会按照定义的顺序随着外部方法的调用而执行。
my_instance.outer_method()
