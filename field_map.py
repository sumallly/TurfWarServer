import numpy as np

class FieldMap:
    field_width = 30
    field_height = 20

    obstacle_block = "*"
    empty_block = " "

    def __init__(self, init) -> None:
        self.field_map = init

    def get_flat_map(self):
        return self.field_map

    @classmethod
    def create_flatmap(cls):
        flatmap = "*"
        for i in range(20*30-1):
            flatmap += "*"
        fm = FieldMap(flatmap)
        return fm
