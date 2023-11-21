class FieldMap:
    # empty 0, obstacle 1, item 2, player 11-

    def __init__(self, worldtype = "flat", fieldsize = {'x':30, 'y':20}) -> None:
        self.d = {"empty":0, "obstacle":1, "item":2}
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
                    fieldstr += ('a' + unit - 11)
                else:
                    fieldstr += ' '
        return fieldstr
    
    def add_player(self, ID:str) -> None:
        self.d[ID] = self.userNum + 11
        self.userNum += 1
    
    def get_can_be_painted(self, x, y) -> list:
        return [self.field[y-1][x] != self.d["obstacle"],
                self.field[y][x-1] != self.d["obstacle"],
                self.field[y][x+1] != self.d["obstacle"],
                self.field[y+1][x] != self.d["obstacle"]]

    def paint(self, ID:str, x:int, y:int, item:int) -> int:
        status = 0
        if self.field[y][x] == self.d["obstacle"]:
            status =  -1
        else:    
            if  self.field[y][x] == self.d["item"]:
                status += 1
            self.field[y][x] = self.d[ID]
        return status