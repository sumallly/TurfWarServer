class ServerResponse:
    def __init__(self) -> None:
        self.map = ""
        self.behavior = ""
        self.your_turn = 0

    def set_fieldmap(self, map):
        self.map = map

    def set_behavior(self, up, down, left, right):
        """
        all direction
        set_behavior(1, 1, 1, 1)

        upward direction is unavailable
        set_behavior(0, 1, 1, 1)
        """
        self.behavior = str(up) + str(down) + str(left) + str(right)

    def set_turn(self, flag):
        self.your_turn = flag

    def get_response(self):
        response = self.map + "," + self.behavior + "," + str(self.your_turn)
        return response.encode()
