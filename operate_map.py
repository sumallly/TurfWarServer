from cmath import pi
from random import randint
import random
import copy


class OperateField:
    fieldtype_dict = {"flat":0, "circular":1, "grid":2, "complicated":3}
    @classmethod
    def get_field_type(cls):
        return cls.fieldtype_dict

    def __init__(self, fieldtype, fieldsize) -> None:
        self.field = [[0 for j in range(fieldsize['x'])] for i in range(fieldsize['y'])]
        self.d = {"empty":0, "obstacle":1, "item":2}
        self.fieldsize = fieldsize
        
        for i, row in enumerate(self.field):
            if i == 0 or i == len(self.field)-1:
                for j in range(len(row)):
                    row[j] = 1
            row[0] = row[fieldsize['x'] - 1] = 1

        if fieldtype:
            if fieldtype == self.fieldtype_dict["circular"]:
                self.__add_obstacle_circular()
            elif fieldtype == self.fieldtype_dict["grid"]:
                self.__add_obstacle_grid()
            elif fieldtype == self.fieldtype_dict["complicated"]:
                self.__add_obstacle_complicated()
                self.__fill_isolated_area()
            else:
                pass
    
    def __add_obstacle_circular(self):
        yL = len(self.field)
        xL = len(self.field[0])
        for y in range(yL):
            for x in range(xL):
                if ((x-xL/2+0.5)/xL)**2 + ((y-yL/2+0.5)/yL)**2 > 0.2:
                    self.field[y][x] = 1
    
    def __add_obstacle_grid(self):
        for i, row in enumerate(self.field):
            if i%2 == 0:
                for i in range(int(len(row)/2)):
                    row[i*2] = 1

    def __add_obstacle_complicated(self):
        for i in range(int(self.fieldsize["x"]*self.fieldsize["y"] / 6.0)):
            pos = self.__get_random_pos(0)
            self.field[pos[0]][pos[1]] = 1
        # add obstacle to isolated area

    def __get_random_pos(self, objtype_place):
        if type(objtype_place) == int:
            objtype_place = [objtype_place]
        pos = [randint(1, self.fieldsize["y"]-2), randint(1, self.fieldsize["x"]-2)]
        while not self.field[pos[0]][pos[1]] in objtype_place:
            pos = [randint(1, self.fieldsize["y"]-2), randint(1, self.fieldsize["x"]-2)]
        return pos

    def __fill_isolated_area(self):
        checkfield = copy.deepcopy(self.field)
        # mapping numbers for each isolated area by scanning field
        thereisblank = True
        checknum = -1
        while thereisblank:
            for i in range(len(checkfield)):
                for j in range(len(row)):
                    if checkfield[i][j] == 0:
                        checkfield[i][j] = checknum
                        checknum -= 1
                        break
                else:
                    continue
                break
                

            for row in checkfield:
                if 0 in row:
                    checkfield = True
                    break
                else:
                    checkfield = False    
                    

    def get_init_position(self, angle = None) -> list:
        if angle is None:
            angle = random.uniform(0.0, 2*pi)
		# Farthest point by angle from center
        return self.__get_random_pos(0)
	
    def place_item(self) -> None:
        pos = [randint(1, self.fieldsize["y"]-1), randint(1, self.fieldsize["x"]-1)]
        while self.field[pos[0]][pos[1]] == 1:
            pos = [randint(1, self.fieldsize["y"]-1), randint(1, self.fieldsize["x"]-1)]
        self.field[pos[0]][pos[1]] = 2

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