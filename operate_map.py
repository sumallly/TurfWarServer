from cmath import pi
import random


class OperateField:
    @classmethod
    def get_field_type(cls):
        return ["flat", "circular", "grid", "complicated"]

	def __init__(self, fieldtype, fieldsize) -> None:
		self.field = [[0 for j in range(fieldsize['x'])] for i in range(fieldsize['y'])]
        self.d = {"empty":0, "obstacle":1, "item":2}

        for row in self.field:
            row[0] = row[fieldsize['x'] - 1] = 1

		if fieldtype:
            # generate field process by fieldtype
            pass

	def get_init_position(angle = None) -> list:
		if angle is None:
			angle = random.uniform(0.0, 2*pi)
		# Farthest point by angle from center
		return [randint(1, fieldsize["y"]-1), randint(1, fieldsize["x"]-1)]
	
	def can_be_painted(self, position:list) -> list:
        y = position[0]
        x = position[1]
        return [self.field[y-1][x] != self.d["obstacle"],
                self.field[y][x-1] != self.d["obstacle"],
                self.field[y][x+1] != self.d["obstacle"],
                self.field[y+1][x] != self.d["obstacle"]]

    def paint_by_position(self, color:int, position:list, item:int) -> int:
        y = position[0]
        x = position[1]
        status = 0
        if self.field[y][x] == self.d["obstacle"]:
            status =  -1
        else:    
            if self.field[y][x] == self.d["item"]:
                status += 1

            if item:
                #process by item
                pass

            self.field[y][x] = color
        return status