from random import randint
from items import ItemTemplate

class FieldMap:
    # empty 0, obstacle 1, item 2, player 11-

    def __init__(self, worldtype = "flat", fieldsize = {'x':30, 'y':20}) -> None:
        self.d = {"empty":0, "obstacle":1, "item":2}
        self.position = {}
        self.symbol = {}
        self.userNum = 0

        self.field = [[0 for j in range(fieldsize['x'])] for i in range(fieldsize['y'])]
        for row in self.field:
            row[0] = row[fieldsize['x'] - 1] = 1

        if worldtype == "flat":
            pass
        # elif worldtype = "def"

    def get_map_raw(self) -> list:
        return self.field

    def get_map_sendable(self) -> str:
        fieldstr = ""
        for row in self.field:
            for unit in row:
                if unit == 1:
                    fieldstr += '*'
                elif unit == 2:
                    fieldstr += '?'
                elif unit > 10:
                    # process by player
                    fieldstr += self.symbol[unit]
                else:
                    fieldstr += ' '
        return fieldstr

    def add_player(self, ID:str, mark:str) -> None:
        self.d[ID] = self.userNum + 11
        self.position[self.d[ID]] = [randint(1, 19), randint(1, 29)]
            # [y, x] make func init position
        self.symbol[self.d[ID]] = mark
            # make func generate random symbol by user
        self.userNum += 1

    def get_can_be_painted_direction(self, ID:str):
        return self.__can_be_painted(self.position[self.d[ID]])

    def __can_be_painted(self, position:list) -> list:
        y = position[0]
        x = position[1]
        return [self.field[y-1][x] != self.d["obstacle"],
                self.field[y][x-1] != self.d["obstacle"],
                self.field[y][x+1] != self.d["obstacle"],
                self.field[y+1][x] != self.d["obstacle"]]

    def paint_by_direction(self, ID:str, direction:str, item:int) -> int:
        pos = self.position[self.d[ID]]
        if direction == "w":
            pos[0] -= 1
        elif direction == "a":
            pos[1] -= 1
        elif direction == "s":
            pos[1] += 1
        elif direction == "d":
            pos[0] += 1
        else:
            # invalid direction charactor
            pass
        return self.__paint_by_position(ID, pos, item)

    def paint_by_item(self, ID:str, item: ItemTemplate):
        player_position = self.position[self.d[ID]]
        mask = item.get_mask(player_position)

        for i, row in enumerate(mask):
            for j, flag in enumerate(row):
                if flag == 0:
                    continue

                self.__paint_by_position(ID, (i, j), 0)

    def __paint_by_position(self, ID:str, position:list, item:int) -> int:
        y = position[0]
        x = position[1]
        status = 0
        if self.field[y][x] == self.d["obstacle"]:
            status =  -1
        else:
            if self.field[y][x] == self.d["item"]:
                # process by item
                status += 1
            self.field[y][x] = self.d[ID]
        return status
