import numpy as np

class ItemTemplate:
    def __init__(self) -> None:
        self.paint_area = []
        self.item_no = -1

    def get_mask(self, position):
        player_x = position[1]
        player_y = position[0]
        mask = np.zeros((20, 30), dtype=np.uint8)

        for i, row in enumerate(self.paint_area):
            for j, flag in enumerate(row):
                if flag == 0:
                    continue
                mask[i + player_y - 2][j + player_x - 2] = 1

        return mask.tolist()

