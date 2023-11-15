from field_map import FieldMap

class TurfWarGame:
    def __init__(self) -> None:
        self.fm = FieldMap.create_flatmap()

    def get_map(self):
        return self.fm.get_flat_map()

    def step(self):
        pass
