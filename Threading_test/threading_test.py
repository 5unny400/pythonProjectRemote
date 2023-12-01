"""
@FileName：threading_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/1
"""
import threading


def my_function():
    print("This is a thread.")


# 创建线程对象
my_thread = threading.Thread(target=my_function)

# 启动线程
my_thread.start()
