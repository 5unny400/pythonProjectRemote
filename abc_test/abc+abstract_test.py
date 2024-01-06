from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# 下面的代码会报错，因为抽象基类 Shape 中的抽象方法 area 必须在子类中被实现
# shape = Shape()

# 创建 Circle 和 Square 的实例，并调用它们的 area 方法
circle = Circle(radius=5)
square = Square(side=4)

print(circle.area())  # 输出圆的面积
print(square.area())  # 输出正方形的面积
