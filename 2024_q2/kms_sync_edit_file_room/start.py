import json

from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

rooms = {}  # Dictionary to store active rooms and their connection counts
data_dict = {}  # Dictionary to store data for each doc_id

# Dictionary to store last heartbeat time and doc_id for each client
doc_id_and_last_activity_times_for_clients = []


def check_room_connections():
    # Check if there are any rooms with zero connections
    while True:
        rooms_to_remove = [doc_id for doc_id, count in rooms.items() if count == 0]
        for doc_id in rooms_to_remove:
            del rooms[doc_id]
            print("Room {} has no connections, removing it".format(doc_id))
            print("未合并的 crdt存入数据库......")
        reduce_inactive_connections()
        time.sleep(5)  # Check every 5 seconds




def reduce_inactive_connections():
    # Reduce count for inactive connections
    for doc_id, count in rooms.items():
        if count > 0 and doc_id in data_dict:
            last_activity_time = data_dict[doc_id][-1].get('timestamp', 0)
            # If last activity time is more than 10 seconds ago, reduce count by 1
            if time.time() - last_activity_time > 10:
                rooms[doc_id] -= 1
                print(f"Reducing connection count for room {doc_id} due to inactivity")

# 监听心跳事件，更新对应的连接的last_activity_time
@socketio.on('heartbeat')
def handle_heartbeat(data):
    doc_id = data['doc_id']
    if doc_id in data_dict:
        data_dict[doc_id][-1]['timestamp'] = time.time()
        print(f"Received heartbeat from room {doc_id}")

@socketio.on('connect')
def handle_connect():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Client connected")


@socketio.on('disconnect')
def handle_disconnect():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "Client disconnected")


@socketio.on('message')
def handle_message(data):

    data = data.get('data')
    doc_id = data['doc_id']

    if doc_id:
        join_room(doc_id)  # Join the room based on the doc_id
        rooms[doc_id] = rooms.get(doc_id, 0) + 1  # Increment connection count for the doc_id

        print("Received message from room {}: {}".format(doc_id, data))
        # Update data_dict
        if doc_id not in data_dict:
            data_dict[doc_id] = []
        data_dict[doc_id].append(data)

        # 同步信息示例
        sync_data = data_dict[doc_id]
        emit('message', sync_data, room=doc_id)


if __name__ == '__main__':
    threading.Thread(target=check_room_connections, daemon=True).start()
    socketio.run(app, port=5999, debug=False, allow_unsafe_werkzeug=True)
