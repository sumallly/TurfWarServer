import socket
import threading

class TcpServer:
    def __init__(self, ip, port) -> None:
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server.bind((ip, port))
        self.tcp_server.listen()

        self.callback = None

    def start_accept(self):
        accept_result = self.tcp_server.accept()
        thread = threading.Thread(target=self.callback, args=accept_result)
        thread.start()

    def register_callback(self, callback_fct):
        self.callback = callback_fct
