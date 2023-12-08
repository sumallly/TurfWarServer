class ServerResponse:
    def __init__(self) -> None:
        self.map = ""
        self.behavior = ""
        self.field_w = 31
        self.field_h = 21
        self.have_item = 0
        self.x = -1
        self.y = -1
        self.is_end = 0

    def set_fieldmap(self, map):
        self.map = map

    def set_behavior(self, up, left, right, down):
        """
        all direction
        set_behavior(1, 1, 1, 1)

        upward direction is unavailable
        set_behavior(0, 1, 1, 1)
        """
        self.behavior = str(up) + str(left) + str(right) + str(down)

    def set_having_item(self, flag):
        self.have_item = flag

    def set_player_position(self, pos):
        self.x = pos[1]
        self.y = pos[0]
        
    def set_endflag(self):
        self.is_end = 1

    def get_response(self):
        msgs = [
            self.map,
            self.behavior,
            self.field_w,
            self.field_h,
            self.have_item,
            self.x,
            self.y,
            self.is_end
        ]

        response = msgs[0]
        for msg in msgs[1:]:
            response += ","
            response += str(msg)

        return response.encode()
