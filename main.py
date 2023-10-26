import time
from tcp_server import TcpServer


def callback_accept(client, addr):
    print(type(addr))
    for i in range(10):
        client.send(b"test")
        time.sleep(1)
    client.close()


def main():
    tcp_server = TcpServer("127.0.0.1", 8000)
    tcp_server.register_callback(callback_accept)

    while True:
        try:
            tcp_server.start_accept()
        except KeyboardInterrupt:
            print("Shutdown server ...")
            break
        except BrokenPipeError:
            print("Broke pipe")
            pass


if __name__ == "__main__":
    main()
