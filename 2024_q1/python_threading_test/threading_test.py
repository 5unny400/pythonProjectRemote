"""
@FileName：threading_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/16
"""
import threading

# 创建一个thread-local对象
local_data = threading.local()

# 在一个线程中设置值
def set_value(value):
    local_data.value = value

# 在另一个线程中获取值
def get_value():
    return local_data.value if hasattr(local_data, 'value') else None

# 示例使用两个线程
def worker1():
    set_value(10)
    print(f"Worker 1: {get_value()}")

def worker2():
    set_value(20)
    print(f"Worker 2: {get_value()}")

# 创建两个线程并启动它们
thread1 = threading.Thread(target=worker1)
thread2 = threading.Thread(target=worker2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()