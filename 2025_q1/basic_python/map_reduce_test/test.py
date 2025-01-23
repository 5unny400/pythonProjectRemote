"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/21
"""
def f(x):
    return x * x

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))
# 13579


from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int("2378"))


# 还可以用lambda函数进一步简化成：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str22int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str22int("782389"))