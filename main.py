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

    game: TurfWarGame = games[session_id]

    gs.wait_for_opponents(session_id)

    print(f"Start game(id={session_id}, p={player_num})")

    try:
        while True:
            # Server -> Client
            server_res_msg = game.get_response(player_num)
            client.send(server_res_msg)
            print(f"Server -> Client(id={session_id}, p={player_num})")

            # Client -> Server
            client_res_msg =  client.recv(256)
            
            if game.step(player_num, client_res_msg):
                print(f"Client(id={session_id}, p={player_num}) -> Server")
                game.wait_other_player()
            else :
                print(f"This game is closed. id: ({session_id})")
                break

    except BrokenPipeError:
        print(f"Broken pipe id: ({session_id})")
        # gs.remove_from_id(session_id)
    
    finally:
        print(f"Close client id: ({session_id})")
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

    print("end")

if __name__ == "__main__":
    main()
