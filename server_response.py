class ServerResponse:
    def __init__(self) -> None:
        self.map = ""
        self.behavior = ""
        self.field_w = 31
        self.field_h = 21
        self.have_item = 0

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
        
    def set_having_item(self, flag):
        self.have_item = flag

    def get_response(self):
        response = self.map + "," + self.behavior + "," + str(self.field_w) + "," + str(self.field_h) + "," + str(self.have_item)
        return response.encode()
