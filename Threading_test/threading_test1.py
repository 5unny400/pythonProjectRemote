"""
@FileName：threading_test1.py
@Description：
@Author：shenxinyuan
@Time：2023/12/1
"""
import threading

shared_variable = 0
lock = threading.Lock()


def increment_variable():
    global shared_variable
    # 加锁
    with lock:
        shared_variable += 1


# 创建多个线程并启动
threads = [threading.Thread(target=increment_variable) for _ in range(5)]
for thread in threads:
    thread.start()

# 等待所有线程执行完毕
for thread in threads:
    thread.join()

print("Final value of shared variable:", shared_variable)
