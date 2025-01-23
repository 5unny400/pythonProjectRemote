"""
@FileName：test
@Description：  打印斐波那契数列的骚操作
@Author：shenxinyuan
@Time：2025/1/21
"""
class Fib(object):
    def __init__(self, max_num: int = 1000):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
        self.max_num = max_num

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    # 可以向列表一样被迭代
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > self.max_num: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    # 可以像列表一样取某个下标的元素
    # def __getitem__(self, n):
    #     a, b = 1, 1
    #     for x in range(n):
    #         a, b = b, a + b
    #     return a

    # 不但可以根据下标取元素而且可以切片
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


fib = Fib()
for n in fib:
    print(n)

print("根据下标取元素")
print(fib[0])
print(fib[3])

print("切片")
print(fib[0:5])