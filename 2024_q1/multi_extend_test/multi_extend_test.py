"""
@FileName：multi_extend_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/15
"""


class Parent1:
    def method(self):
        print("This is from parent class 1")


class Parent2:
    def method(self):
        print("This is from parent class 2")


class Child(Parent1, Parent2):
    pass


class Child2(Parent2, Parent1):
    pass


child = Child()
child.method()  # 输出 "This is from parent class 1"
# Child定义了两个父类Parent1和Parent2，每个父类都包含了一个名为method()的方法。然后通过多重继承将这两个父类合并到子类Child中。
# 最后创建子类对象child并调用其method()方法，结果会打印出"This is from parent class 1"。

child2 = Child2()
child2.method()  # 输出 "This is from parent class 2"
# Child2定义了两个父类Parent2和Parent1，每个父类都包含了一个名为method()的方法。然后通过多重继承将这两个父类合并到子类Child中。
# 最后创建子类对象child并调用其method()方法，结果会打印出"This is from parent class 2"。

