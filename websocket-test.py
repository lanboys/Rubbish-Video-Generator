import websocket

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection established")
    # 向服务器发送消息
    ws.send("Hello, server!")

if __name__ == "__main__":
    # 创建 websocket 连接
    ws = websocket.WebSocketApp("ws://localhost:8080",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    # 开始连接
    ws.run_forever()
