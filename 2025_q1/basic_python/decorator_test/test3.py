"""
@FileName：test3
@Description：
@Author：shenxinyuan
@Time：2025/1/21
"""
import time, functools


def metric(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = func(*args, **kwargs)
        end_time = time.time()
        print('%s executed in %s ms' % (func.__name__, end_time - start_time))
        return process

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')