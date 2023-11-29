from cmath import pi
from random import randint
import random
import copy


class OperateField:
    fieldtype_dict = {"flat":0, "circular":1, "grid":2, "complicated":3}
    @classmethod
    def get_field_type(cls):
        return cls.fieldtype_dict

    def __init__(self, fieldtype, fieldsize, density) -> None:
        self.field = [[0 for j in range(fieldsize['x'])] for i in range(fieldsize['y'])]
        self.d = {"empty":0, "obstacle":1, "item":2}
        self.fieldsize = fieldsize
        self.density = density

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
                if ((x-xL/2+0.5)/xL)**2 + ((y-yL/2+0.5)/yL)**2 > (0.25 - 0.005*self.density):
                    self.field[y][x] = 1

    def __add_obstacle_grid(self):
        # add density system
        for i, row in enumerate(self.field):
            if i%2 == 0:
                for i in range(int(len(row)/2)):
                    row[i*2] = 1

    def __add_obstacle_complicated(self):
        for i in range(int(self.fieldsize["x"]*self.fieldsize["y"] / (60/self.density))):
            pos = self.__get_random_pos(0)
            self.field[pos[0]][pos[1]] = 1
        # add obstacle to isolated area

    def __get_random_pos(self, objtype_place = None, objtype_avoid = None):
        if objtype_place == objtype_avoid == None:
            return None
        
        if type(objtype_place) == int:
            objtype_place = [objtype_place]
        elif type(objtype_avoid) == int:
            objtype_avoid = [objtype_avoid]

        
        pos = [randint(1, self.fieldsize["y"]-2), randint(1, self.fieldsize["x"]-2)]
        if objtype_place != None:
            while not self.field[pos[0]][pos[1]] in objtype_place:
                pos = [randint(1, self.fieldsize["y"]-2), randint(1, self.fieldsize["x"]-2)]
        elif objtype_avoid != None:
            while self.field[pos[0]][pos[1]] in objtype_avoid:
                pos = [randint(1, self.fieldsize["y"]-2), randint(1, self.fieldsize["x"]-2)]
        return pos

    def __fill_isolated_area(self) -> None:
        checkfield = copy.deepcopy(self.field)
        # mapping numbers for each isolated area by scanning field
        thereisblank = True
        checknum = -1
        while thereisblank:
            for i in range(len(checkfield)):
                for j in range(len(checkfield[0])):
                    if checkfield[i][j] == 0:
                        checkfield[i][j] = checknum
                        break
                else:
                    continue
                break

            for k in range(2*max(len(checkfield), len(checkfield[0]))):
                for i in range(len(checkfield)):
                    for j in range(len(checkfield[0])):
                        if checkfield[i][j] == checknum:
                            self.__paint_around_if_blank(checkfield, [i, j], checknum)

            checknum -= 1
            for row in checkfield:
                if 0 in row:
                    thereisblank = True
                    break
                else:
                    thereisblank = False

        maxareanum = self.__count_by_checknum(checkfield)
        # print(maxareanum)
        for i in range(len(checkfield)):
            for j in range(len(checkfield[0])):
                if checkfield[i][j] != -1*maxareanum:
                    self.field[i][j] = 1

    def __paint_around_if_blank(self, checkfield, pos, paint_by) -> None:
        self.__paint_if(checkfield, [pos[0]-1, pos[1]], paint_by, 0)
        self.__paint_if(checkfield, [pos[0], pos[1]-1], paint_by, 0)
        self.__paint_if(checkfield, [pos[0], pos[1]+1], paint_by, 0)
        self.__paint_if(checkfield, [pos[0]+1, pos[1]], paint_by, 0)

    def __paint_if(self, checkfield, pos, paint_by, origin) -> None:
        if checkfield[pos[0]][pos[1]] == origin:
            # print(pos, paint_by, origin)
            checkfield[pos[0]][pos[1]] = paint_by

    def __count_by_checknum(self, checkfield) -> list:
        ischecked = False
        maxcheck = int(len(checkfield)*len(checkfield[0])/2)
        arealist = [0 for i in range(maxcheck)]

        for i in range(len(checkfield)):
            for j in range(len(checkfield[0])):
                if checkfield[i][j] < 0:
                    arealist[-1*checkfield[i][j]] += 1

        i = 0
        for i in range(1, maxcheck):
            if arealist[i] == 0:
                break
        # print(arealist)
        del arealist[i:]
        return arealist.index(max(arealist))

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
