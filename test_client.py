# -*- coding : UTF-8 -*-

# 0.ライブラリのインポートと変数定義
import socket

target_ip = "127.0.0.1"
target_port = 8000
buffer_size = 4096

def display_map(raw):
    w = 30
    h = 20
    for i in range(h):
        for j in range(w):
            print(raw[i*w+j], end="")
        print()

# 1.ソケットオブジェクトの作成
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.サーバに接続
tcp_client.connect((target_ip,target_port))
while True:
    response = tcp_client.recv(buffer_size).decode()
    res_msgs = response.split(",")
    display_map(res_msgs[0])

    print("input=")
    cli_msg = input()
    tcp_client.send(cli_msg.encode())
