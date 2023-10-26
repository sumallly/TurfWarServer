# -*- coding : UTF-8 -*-

# 0.ライブラリのインポートと変数定義
import socket

target_ip = "127.0.0.1"
target_port = 8000
buffer_size = 4096

# 1.ソケットオブジェクトの作成
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.サーバに接続
tcp_client.connect((target_ip,target_port))
while True:
    response = tcp_client.recv(buffer_size).decode()
    if response == "":
        continue
    print("[*]Received a response : {}".format(response))
