from field_map import FieldMap
from client_message import ClientMessage
from server_response import ServerResponse

class TurfWarGame:
    def __init__(self) -> None:
        self.fm = FieldMap()
        self.which_turn = 0

        self.responses = [ServerResponse(), ServerResponse()]

        self.num_of_res = 0

    def get_map(self):
        return self.fm.get_map_sendable()

    def get_response(self, id):
        res = self.responses[id]

        res.set_behavior(1, 1, 1, 1)
        res.set_fieldmap(self.get_map())

        this_p_turn_is = int(self.which_turn == id)
        res.set_turn(this_p_turn_is)

        return res.get_response()

    def step(self, p_id, message):
        self.num_of_res += 1

        msg = ClientMessage(message)

        map = self.get_map()
        # updated_map = map.paint()

    def wait_other_player(self):
        while self.num_of_res != 2:
            pass
