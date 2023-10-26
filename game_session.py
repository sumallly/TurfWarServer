class GameSession:
    def __init__(self) -> None:
        self.players = {}

    def init_player(self):
        registerd_player_num = len(self.players)

        id = int(registerd_player_num // 2)
        num = int(registerd_player_num % 2)

        return id, num

    def inquiry(self, addr):
        if addr not in self.players:
            self.players[addr] = self.init_player()

        return self.players[addr]

