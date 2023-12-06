"""
@FileName：py_inner_methoeds_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/6
"""
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

obj = MyClass("value1", "value2")

class MyMeta(type):
    def __prepare__(cls, name, bases):
        # 返回一个自定义的命名空间，例如使用 OrderedDict
        return collections.OrderedDict()

class MyClass(metaclass=MyMeta):
    def method(self):
        pass


"""
Python 中有许多特殊方法（也称为魔法方法或双下划线方法），它们以双下划线开头和结尾。这些方法用于在类中提供特定行为。以下是一些常见的内置方法：

1. **`__new__`：**
   - 在 `__init__` 方法之前调用，用于创建对象实例。
   - 通常用于自定义不可变类型或基于条件的对象创建。

2. **`__del__`：**
   - 在对象被删除（垃圾回收）之前调用。
   - 可以用于执行清理操作。

3. **`__str__` 和 `__repr__`：**
   - `__str__` 用于返回对象的字符串表示，通常由 `str()` 调用。
   - `__repr__` 用于返回对象的“官方”字符串表示，通常由 `repr()` 调用。

4. **`__len__`：**
   - 定义对象的长度，由内置函数 `len()` 调用。

5. **`__getitem__` 和 `__setitem__`：**
   - `__getitem__` 用于获取对象的元素，由索引运算符 `[]` 调用。
   - `__setitem__` 用于设置对象的元素。

6. **`__iter__` 和 `__next__`：**
   - `__iter__` 用于返回一个迭代器对象，通常在实现迭代协议时使用。
   - `__next__` 用于在迭代器中获取下一个值。

7. **`__call__`：**
   - 允许将类实例像函数一样调用。

8. **`__contains__`：**
   - 定义 `in` 运算符的行为。

9. **`__eq__`、`__ne__`、`__lt__`、`__le__`、`__gt__`、`__ge__`：**
   - 用于定义对象的比较操作。

10. **`__hash__`：**
    - 用于返回对象的哈希值，通常在实现自定义哈希的不可变对象时使用。

这只是其中一部分，Python 中还有许多其他特殊方法，每个方法都有其特定的用途。在需要自定义类的行为时，你可以根据需要选择实现这些方法。
"""