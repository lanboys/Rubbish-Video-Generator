import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import io
import os
import subprocess
import math
from time import sleep
from moviepy.editor import *
import wave, audioop

from run import getText, Ws_Param


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
    getText('args.txt')  # 台词写入文本

    # 获取APPID、APIKey、APISecret
    APPID, APIKey, APISecret = '', '', ''
    with open('args.txt',encoding="utf-8") as f:
        APPID, APIKey, APISecret = f.readlines()[3].strip().split(';')

        # 文本转人声

    wsParam = Ws_Param(APPID=APPID, APIKey=APIKey, APISecret=APISecret,
                       Text="大家可能会很惊讶核桃核怎么会不能吞下去呢")
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever( )
