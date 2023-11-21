from field_map import FieldMap
from client_message import ClientMessage
from server_response import ServerResponse
import time

class TurfWarGame:
    def __init__(self) -> None:
        self.fm: FieldMap = FieldMap()
        self.fm.add_player("0", "o")
        self.fm.add_player("1", "x")

        self.which_turn = 0

        self.responses = [ServerResponse(), ServerResponse()]

        self.num_of_res = 0
        self.turn = 2

    def get_map(self):
        return self.fm.get_map_sendable()

    def get_response(self, id):
        res = self.responses[id]

        can_behavior = self.fm.get_can_be_painted_direction(str(id))
        res.set_behavior(*can_behavior)
        res.set_fieldmap(self.get_map())

        this_p_turn_is = int(self.which_turn == id)
        res.set_turn(this_p_turn_is)

        return res.get_response()

    def step(self, p_id, message):
        self.num_of_res += 1

        msg = ClientMessage(message)

        move_dir = msg.get_behavior()
        self.fm.paint_by_direction(str(p_id), move_dir, 0)

    def wait_other_player(self):
        while self.num_of_res != self.turn:
            pass

        time.sleep(0.2)
        self.turn += 1

