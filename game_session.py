class GameSession:
    def __init__(self) -> None:
        self.players = {}

    def __init_player(self):
        registerd_player_num = len(self.players)

        id = int(registerd_player_num // 2)
        num = int(registerd_player_num % 2)

        return id, num

    def register(self, addr):
        if addr in self.players:
            raise ValueError("This address is already registerd.")

        self.players[addr] = self.__init_player()

    def inquiry(self, addr):
        if addr not in self.players:
            raise ValueError("This address is not registerd")

        return self.players[addr]

    def remove(self, addr):
        self.players.pop(addr)
