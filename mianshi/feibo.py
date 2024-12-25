# 实现一个装饰器，打印被装饰函数的执行时间。
import time
from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"函数 {func.__name__} 执行时间为: {end_time - start_time} 秒")
        return result
    return wrapper

# 命令行读取参数N，打印斐波那契数列前N位
#1 1 2 3 5 8
@timer
def feibo(num: int):
    if num == 1 or num == 2:
        return 1
    return feibo(num - 1) + feibo(num - 2)

@timer
def feibo2(num: int, feibo_list: list):
    time.sleep(0.1)
    if num == 1 or num == 2:
        return 1
    if not feibo_list[num - 1]:
        feibo_list[num - 1] = feibo2(num - 1, feibo_list)
    if not feibo_list[num - 2]:
        feibo_list[num - 2] = feibo2(num - 2, feibo_list)
    return feibo_list[num - 1] + feibo_list[num - 2]


if __name__ == '__main__':
    import sys

    # num = int(sys.argv[1])  # 获取命令行参数并去除第一个元素（脚本文件名）
    # print(num)

    num = int(input("请输入要打印的斐波那契数列位数："))
    feibo_list = [0 for i in range(1, num)]

    for i in range(1, num):
        print(str(feibo2(i, feibo_list)) + " ")