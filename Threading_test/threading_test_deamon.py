"""
@FileName：threading_test_deamon.py
@Description：守护线程
@Author：shenxinyuan
@Time：2023/12/1
"""
import threading
import time


def daemon_function():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)


# 创建守护线程
daemon_thread = threading.Thread(target=daemon_function)
daemon_thread.daemon = True  # 将线程设置为守护线程

# 启动守护线程
daemon_thread.start()

# 主线程执行其他任务
time.sleep(3)
print("Main thread is done.")
