from item_template import ItemTemplate

class VerticalPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        self.paint_area = [ \
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0]
        ]

        self.item_no = 1

class HorizontalPaintItem(ItemTemplate):
    def __init__(self) -> None:
        super().__init__()

        super().paint_area = [ \
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        super().item_no = 2

