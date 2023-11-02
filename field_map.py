import numpy as np

class FieldMap:
    field_width = 30
    field_height = 20
    
    def __init__(self) -> None:
        self.field_map = np.zeros((self.field_height, self.field_width))
    
    def get_2d_map(self):
        return self.field_map
    
    def get_flatten_map(self):
        return self.field_map.flatten()
    
    def paint_at(self, x, y, to):
        self.field_map[y][x] = to