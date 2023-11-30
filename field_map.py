from random import randint
from operate_map import OperateField
from items import VerticalPaintItem, ItemTemplate

class FieldMap:
    # empty 0, obstacle 1, item 2, player 11-

    @classmethod
    def get_field_type(cls) -> dict:
        return OperateField.get_field_type()

    def __init__(self, fieldtype = None, fieldsize = {'x':31, 'y':21}, density = 10) -> None:
        self.position = {}
        self.symbols = {}
        self.userNum = 0

        if fieldtype is None:
            fieldtype = 0
        
        self.operator = OperateField(fieldtype, fieldsize, density)
        self.d = self.operator.d

    def get_map_raw(self) -> list:
        return self.operator.field

    def get_map_sendable(self) -> str:
        fieldstr = ""
        for row in self.operator.field:
            for unit in row:
                if unit == 1:
                    fieldstr += '*'
                elif unit == 2:
                    fieldstr += '?'
                elif unit > 10:
                    fieldstr += self.symbols[unit]
                else:
                    fieldstr += ' '
                fieldstr += ' '
        return fieldstr

    def add_player(self, ID:str, symbol:str) -> None:
        self.d[ID] = self.userNum + 11
        self.position[self.d[ID]] = self.operator.get_init_position()
        self.symbols[self.d[ID]] = symbol
        self.operator.paint_by_position(self.d[ID], self.position[self.d[ID]])
        self.userNum += 1

    def get_user_position(self, ID:str) -> list:
        return self.position[self.d[ID]]    # [y, x]

    def overwrite_user_position(self, ID:str, position:list) -> None:
        self.position[self.d[ID]] = position

    def get_user_symbol(self, ID:str) -> str:
        return self.symbols[self.d[ID]]

    def overwrite_user_symbol(self, ID:str, symbol:str) -> None:
        self.symbols[self.d[ID]] = symbol

    def get_field_size(self):
        return self.operator.fieldsize
    
    def get_can_be_painted_direction(self, ID:str):
        return self.operator.can_be_painted(self.position[self.d[ID]])

    def paint_by_direction(self, ID:str, direction:str) -> int:
        pos = self.position[self.d[ID]]
        x = y = 0
        if direction == "w":
            y -= 1
        elif direction == "a":
            x -= 1
        elif direction == "d":
            x += 1
        elif direction == "s":
            y += 1
        else:
            # invalid direction charactor
            pass
        if self.operator.field[pos[0]+y][pos[1]+x] != 1:
            pos[0] += y
            pos[1] += x
        return self.operator.paint_by_position(self.d[ID], pos)

    def place_item(self) -> None:
        # avoid player
        self.operator.place_item()

    def paint_by_item(self, ID:str, item: ItemTemplate):
        player_position = self.position[self.d[ID]]
        mask = item.get_mask(player_position)

        for i, row in enumerate(mask):
            for j, flag in enumerate(row):
                if flag == 0:
                    continue
                self.operator.paint_by_position(self.d[ID], (i, j))


if __name__ == "__main__":
    print(FieldMap.get_field_type())
    sel = int(input())
    print("dencity (def=10)")
    density = int(input())
    print("fieldsize : x, y")
    size = list(map(int, input().split(",")))
    fm = FieldMap(fieldtype=sel, fieldsize={'x':size[0], 'y':size[1]}, density = density)
    fm.add_player("0", "o")
    fm.add_player("1", "x")
    fm.operator.place_item()

    fm.paint_by_item("0", VerticalPaintItem())

    s = fm.get_map_sendable()
    fieldsize = fm.get_field_size()
    for i in range(fieldsize["y"]):
        print(s[2*i*fieldsize["x"] : 2*(i+1)*fieldsize["x"]])
