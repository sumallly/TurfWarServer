from field_map import FieldMap
from client_message import ClientMessage
from server_response import ServerResponse
import time

class TurfWarGame:
    def __init__(self) -> None:
        self.fm = FieldMap()
        self.which_turn = 0

        self.responses = [ServerResponse(), ServerResponse()]

        self.num_of_res = 0
        self.turn = 2
    
    def next_step(self):
        self.turn += 1
    
    def wait_process(self):
        time.sleep(0.1)

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

        # map udpate

    def wait_other_player(self):
        while self.num_of_res != self.turn:
            pass
        
