"""
@FileName：threading_test_params.py
@Description：
@Author：shenxinyuan
@Time：2023/12/1
"""
import threading


# 1、target： 指定线程要执行的目标函数。这是一个必选参数，通常是一个函数名。
# 2、args： 用于传递给目标函数的参数，是一个元组。如果目标函数需要接受参数，可以通过这个参数传递。
# 3、kwargs： 用于传递给目标函数的关键字参数，是一个字典。如果目标函数需要接受关键字参数，可以通过这个参数传递。
# 4、daemon： 如果设置为 True，将线程设置为守护线程。守护线程会在主线程结束时自动退出。默认值为 False。
# 5、name： 线程的名称。可以通过 threading.current_thread().name 获取当前线程的名称。如果不提供，系统会自动生成一个唯一的名称。

def my_function():
    print("This is a thread.")


# 创建线程对象，并指定目标函数
my_thread = threading.Thread(target=my_function)
