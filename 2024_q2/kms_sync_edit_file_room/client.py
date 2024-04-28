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
                "doc_id": "5678910",
                "timestamp": time.time(),
                "doc_version": 2,
                "content": [
                    {
                        "module": "text",
                        "id": "insertAfter",
                        "user_id": 1,
                        "position": 0,
                        "value": "H",
                        "site_id": "user_id_1",
                        "timestamp": 1649875245000
                    },
                    # {
                    #     "module": "text",
                    #     "id": "delete",
                    #     "user_id": 2,
                    #     "position": 1,
                    #     "value": "e",
                    #     "site_id": "user_id_2",
                    #     "timestamp": 1649875246000
                    # },
                    # {
                    #     "module": "cell",
                    #     "row_index": 1,
                    #     "col_index": 1,
                    #     "id": "insertAfter",
                    #     "user_id": 2,
                    #     "position": 2,
                    #     "value": "l",
                    #     "site_id": "user_id_1",
                    #     "timestamp": 1649875247000
                    # },
                    # {
                    #     "module": "cell",
                    #     "row_index": 1,
                    #     "col_index": 1,
                    #     "id": "delete",
                    #     "user_id": 3,
                    #     "position": 2,
                    #     "value": "l",
                    #     "site_id": "user_id_1",
                    #     "timestamp": 1649875247000
                    # }
                ]
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
