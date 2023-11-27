import numpy as np
import random
import items

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

    @classmethod
    def create_random_item(cls):
        random_value = random.random()
        
        probabilities = [0.5, 0.5]
        item_types = [ items.HorizontalPaintItem(), items.VerticalPaintItem() ]
        
        item: ItemTemplate = ItemTemplate()
        
        temp = 0
        for i, probability in enumerate(probabilities):
            temp += probability
            if random_value < temp:
                item = item_types[i]
                break
        
        return item