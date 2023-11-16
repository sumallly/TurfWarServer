from field_map import FieldMap

class TurfWarGame:
    def __init__(self) -> None:
        self.fm = FieldMap()

    def get_map(self):
        return self.fm.get_map_sendable()

    def step(self, p_id, response):
        pass
