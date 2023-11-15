class GameSession:
    def __init__(self) -> None:
        self.sess_id = {}
        self.player_num = {}

    def __init_player(self):
        registerd_player_num = len(self.sess_id)

        id = int(registerd_player_num // 2)
        num = int(registerd_player_num % 2)

        id_values = list(self.sess_id.values())
        if id_values.count(id) == 2:
            id = max(id_values) + 1

        return id, num

    def register(self, addr):
        if addr in self.sess_id:
            raise ValueError(f"This address({addr}) is already registerd.")

        self.sess_id[addr], self.player_num[addr] = self.__init_player()
        
    def get_join_num(self, id):
        ids = list(self.sess_id.values())
        num = ids.count(id)
        return num

    def inquiry(self, addr):
        if addr not in self.sess_id:
            raise ValueError(f"This address({addr}) is not registerd")

        return self.sess_id[addr], self.player_num[addr]

    def remove_from_id(self, id):
        addrs = [k for k, v in self.sess_id.items() if v == id]

        for addr in addrs:
            self.sess_id.pop(addr)

