# -*- coding : UTF-8 -*-

# 0.ライブラリのインポートと変数定義
import socket
import random

target_ip = "127.0.0.1"
target_port = 8000
buffer_size = 4096

def display_map(raw, x, y):
    fieldsize={'x':31, 'y':21}
    for i in range(fieldsize["y"]):
        for j in range(fieldsize["x"] * 2):
            block = raw[i*fieldsize["x"]*2+j]

            if block == "o":
                block = "\033[31m" + block + "\033[0m"
            if block == "x":
                block = "\033[32m" + block + "\033[0m"

            if j == x * 2 and i == y:
                block = "\033[7m" + block

            print(block, end="")

        print()

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client.connect((target_ip, target_port))
while True:
    response = tcp_client.recv(buffer_size).decode()
    res_msgs = response.split(",")

    try:
        map_raw = res_msgs[0]
        can_behavior = res_msgs[1]
        have_item = int(res_msgs[4])
        player_x = int(res_msgs[5])
        player_y = int(res_msgs[6])
    except:
        continue

    display_map(map_raw, player_x, player_y)

    behavior_list = ["w", "a", "d", "s"]
    while True:
        index = random.randint(0, 3)
        if can_behavior[index] == "1":
            cli_msg = behavior_list[index] + ","
            break

    if have_item:
        cli_msg += str(random.randint(0, 1)) + ","
    else:
        cli_msg += "0" + ","
    cli_msg += "0"

    tcp_client.send(cli_msg.encode())
