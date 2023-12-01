"""
@FileName：threading_test2.py
@Description：生产者消费者
@Author：shenxinyuan
@Time：2023/12/1
"""
import threading
import queue

my_queue = queue.Queue()


def producer():
    for i in range(5):
        my_queue.put(i)


def consumer():
    while True:
        data = my_queue.get()
        if data is None:
            break
        print("Consumed:", data)


# 创建并启动生产者和消费者线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
my_queue.put(None)  # 发送结束信号给消费者线程
consumer_thread.join()
