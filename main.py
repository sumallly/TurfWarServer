import time
from tcp_server import TcpServer
from game_session import GameSession
from turfwar_game import TurfWarGame
from field_map import FieldMap

gs = GameSession()
games = []

def callback_accept(client, addr):
    print(addr)
    gs.register(addr)
    session_id, player_num = gs.inquiry(addr)
    
    if gs.get_join_num(session_id) == 1:
        games.append(TurfWarGame())
    
    try:
        while True:
            if gs.get_join_num(session_id) != 2:
                continue
            
            field_map = games[session_id].get_map()
            
            client.send(field_map.encode())
            responce =  client.recv(256).decode()
            
            games[session_id].step(responce)
            
            
    except BrokenPipeError:
        print(f"close id({session_id})")
        gs.remove_from_id(session_id)
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
