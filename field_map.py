class FieldMap:
    # empty 0, obstacle 1, item 2, player 11-19

    def __init__(self, worldtype = "flat", mapsize = {'x':30, 'y':20}) -> None:
        self.map = [[0 for j in range(mapsize['x'])] for i in range(mapsize['y'])]
        for row in self.map:
            row[0] = row[mapsize['x'] - 1] = 1

        if worldtype == "flat":
            pass
        # elif worldtype = "def"

    def get_map_raw(self):
        return self.map

    def get_map_sendable(self):
        mapstr = ""
        for row in self.map:
            for unit in row:
                if unit == 1:
                    mapstr += '*'
                elif unit == 2:
                    mapstr += '?'
                elif unit > 10:
                    # process by player
                    mapstr += 'x'
                else:
                    mapstr += ' '
        return mapstr

    # def paint
    # def can be painted