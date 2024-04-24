import socketio
import threading
import time

# 创建 SocketIO 实例
sio = socketio.Client()


def send_and_receive_messages():
    # 主循环
    while True:
        # 模拟发送消息
        data = {
            'data': {
                'doc_id': '123456',
                'content': 'Hello, world!',
                'timestamp': time.time()
            }
        }
        sio.emit('message', data)
        # 每隔一段时间发送一次消息
        time.sleep(1000)


# 定义连接成功时的处理函数
@sio.event
def connect():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 'Connected to server')

    # 启动一个新的线程发送和接收消息
    threading.Thread(target=send_and_receive_messages).start()


# 定义断开连接时的处理函数
@sio.event
def disconnect():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), 'Disconnected from server')


# 定义消息接收处理函数
@sio.on('message')
def handle_message(data):
    print('Received message from server:', data)


# 连接到服务器
sio.connect('http://localhost:5999', namespaces=['/'])


# 等待连接关闭
sio.wait()
