from field_map import FieldMap
from client_message import ClientMessage
from server_response import ServerResponse

class TurfWarGame:
    def __init__(self) -> None:
        self.fm = FieldMap()

    def get_map(self):
        return self.fm.get_map_sendable()

    def step(self, p_id, message):
        msg = ClientMessage(message)

        res = ServerResponse()
        res.set_behavior(1, 1, 1, 1)
        res.set_fieldmap = self.get_map()
        res.set_turn(1)

        return res.get_response()
