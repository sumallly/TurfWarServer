import numpy as np

class FieldMap:
    field_width = 6
    field_height = 6

    obstacle_block = "*"
    empty_block = " "

    def __init__(self, init) -> None:
        self.field_map = init

    def get_2d_map(self):
        return self.field_map

    def get_flatten_map(self):
        return self.field_map.flatten()

    def paint_at(self, x, y, to):
        if not(0 <= x < self.field_width) or not(0 <= y < self.field_height):
            raise ValueError("This point is unavailable.")

        if self.field_map[y][x] == self.obstacle_block:
            raise ValueError(f"There is obstacle block at ({x}, {y}).")

        self.field_map[y][x] = to

    @classmethod
    def create_flatmap(cls):
        flatmap = np.array([["*", "*", "*", "*", "*", "*"],
                            ["*", " ", " ", " ", " ", "*"],
                            ["*", " ", " ", " ", " ", "*"],
                            ["*", " ", " ", " ", " ", "*"],
                            ["*", " ", " ", " ", " ", "*"],
                            ["*", "*", "*", "*", "*", "*"]])
        fm = FieldMap(flatmap)
        return fm
