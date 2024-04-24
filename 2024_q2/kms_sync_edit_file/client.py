import asyncio
import datetime
import json

from easy_websocket import EasyClient
from websockets import WebSocketCommonProtocol

client = EasyClient('ws://localhost:5678')

crdt = {
    "doc_id": 7,
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
        {
            "module": "text",
            "id": "delete",
            "user_id": 2,
            "position": 1,
            "value": "e",
            "site_id": "user_id_2",
            "timestamp": 1649875246000
        },
        {
            "module": "cell",
            "row_index": 1,
            "col_index": 1,
            "id": "insertAfter",
            "user_id": 2,
            "position": 2,
            "value": "l",
            "site_id": "user_id_1",
            "timestamp": 1649875247000
        },
        {
            "module": "cell",
            "row_index": 1,
            "col_index": 1,
            "id": "delete",
            "user_id": 3,
            "position": 2,
            "value": "l",
            "site_id": "user_id_1",
            "timestamp": 1649875247000
        }
    ]
}


@client.init_event()
async def auth(websocket: WebSocketCommonProtocol):
    await websocket.send("123456")
    msg = await websocket.recv()
    if msg != "ok":
        await websocket.close(code=1008)


@client.event()
async def on_message(websocket: WebSocketCommonProtocol):
    while True:
        msg = await websocket.recv()
        print(f"Client get message: {msg}")


@client.event()
async def heartbeat(websocket: WebSocketCommonProtocol):
    while True:
        await websocket.send("Heartbeat:" + websocket.host + str(datetime.datetime.now()))
        await asyncio.sleep(30)


@client.event()
async def send_crdt(websocket: WebSocketCommonProtocol):
    while True:
        json_data = json.dumps(crdt)
        await websocket.send("CRDT:" + f"{json_data}")
        await asyncio.sleep(10000)


client.start()
