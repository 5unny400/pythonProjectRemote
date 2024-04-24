import asyncio
import json
import time
from easy_websocket import EasyServer
from websockets import WebSocketCommonProtocol

server = EasyServer("localhost", 5678)

change_num = 0
document_room_list = []
[
    {
        "doc_id": "123456",
        "data": [{"crdt结构1"}, {"crdt结构2"}]
    },
    {
        "doc_id": "12346",
        "data": [{"crdt结构1"}, {"crdt结构2"}]
    }
]

connected_clients = set()

document_session = {}

client_doc_map = {}  # 记录客户端和文档的映射关系

client_last_heartbeat_time = {}  # 记录客户端最后一次心跳时间

@server.init_event()
async def auth(websocket: WebSocketCommonProtocol):
    token = await websocket.recv()
    if token != "123456":
        await websocket.send("error")
        await websocket.close(code=1008, reason="token not expected")
    else:
        connected_clients.add(websocket)  # 将连接的客户端添加到集合中
        # 增加对应文档id的连接数
        doc_id = "获取消息中的文档id"  # 请根据您的具体逻辑获取文档id
        document_session.setdefault(doc_id, 0)
        document_session[doc_id] += 1
        await websocket.send("ok")


async def listen_disconnect():
    # 通过遍历client_last_heartbeat_time字典，找到断开的客户端对应的文档id，并减少连接数
    for client, last_heartbeat_time in client_last_heartbeat_time.items():
        if time.time() - last_heartbeat_time > 100:  # 10秒内没有收到心跳包，判定为断开连接
            doc_id = client_doc_map.get(client)
            if doc_id:
                await on_close(client, doc_id)


async def on_close(websocket: WebSocketCommonProtocol, doc_id: str):
    connected_clients.remove(websocket)  # 从集合中移除断开的客户端
    if doc_id and doc_id in document_session:
        document_session[doc_id] -= 1
        if document_session[doc_id] == 0:  # 当连接数为0时，结束对应会话
            # 进行结束会话的操作，例如清除相应的数据结构等
            document_session.pop(doc_id)
            # 存入数据库或其他持久化存储
            print(f"文档{doc_id}结束会话,持久化存入数据库中..........")
    else:
        print(f"文档{doc_id}不存在")


@server.event()
async def on_message(websocket: WebSocketCommonProtocol):
    while True:
        msg = await websocket.recv()
        connected_clients.add(websocket)  # 将连接的客户端添加到集合中
        # 如果收到的是心跳包，则忽略
        if msg.startswith("Heartbeat"):
            print(f"Server get heartbeat message: {msg}")
            # 更新客户端的最后心跳时间
            client_last_heartbeat_time[websocket] = time.time()
        elif msg.startswith("CRDT"):
            msg = msg.replace("CRDT:", "")
            # 将 msg 转为字典
            msg = json.loads(msg)
            doc_id = msg.get("doc_id")
            crdt_msg = {}
            if doc_id:
                client_doc_map[websocket] = doc_id
                # 将接收的消息添加到对应文档的crdt结构中
            if not any(doc_id == d['doc_id'] for d in document_room_list):
                crdt_msg = {
                    "doc_id": msg.get("doc_id"),
                    "data": [msg]
                }
                document_room_list.append(crdt_msg)
            else:
                for d in document_room_list:
                    if doc_id == d['doc_id']:
                        document_room_list.remove(d)
                        d["data"].append(msg)
                        crdt_msg = d["data"]
                        document_room_list.append(d)
                        pass

            print(f"Server get message: {msg}")
            # 找到具有相同doc_id的客户端并发送更新
            for client in connected_clients:
                if client in client_doc_map and client_doc_map[client] == doc_id:
                    await client.send(str(crdt_msg))
        await listen_disconnect()


@server.event()
async def handle_websocket(websocket: WebSocketCommonProtocol):
    connected_clients.add(websocket)
    asyncio.create_task(send_heartbeat(websocket))


async def send_heartbeat(websocket: WebSocketCommonProtocol):
    while True:
        await websocket.send("Heartbeat to exam connection" + str(time.time()))
        await asyncio.sleep(10)


server.start()
