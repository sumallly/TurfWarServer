# -*- coding : UTF-8 -*-

# 0.ライブラリのインポートと変数定義
import socket

target_ip = "127.0.0.1"
target_port = 8000
buffer_size = 4096

def display_map(raw):
    fieldsize={'x':31, 'y':21}
    for i in range(fieldsize["y"]):
        print(raw[2*i*fieldsize["x"] : 2*(i+1)*fieldsize["x"]])

# 1.ソケットオブジェクトの作成
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.サーバに接続
tcp_client.connect((target_ip,target_port))
while True:
    response = tcp_client.recv(buffer_size).decode()
    res_msgs = response.split(",")
    # print(res_msgs)
    display_map(res_msgs[0])
    print(res_msgs[1])

    print("input=")
    cli_msg = input() + ","
    cli_msg += input() + ",0"
    tcp_client.send(cli_msg.encode())
