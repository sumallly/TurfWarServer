from cmath import pi
from random import randint
from operate_map import OperateField

class FieldMap:
    # empty 0, obstacle 1, item 2, player 11-

    @classmethod
    def get_field_type(cls) -> list:
        return OperateField.get_field_type()

    def __init__(self, fieldtype = None, fieldsize = {'x':30, 'y':20}) -> None:
        self.position = {}
        self.symbols = {}
        self.userNum = 0
        
        if worldtype is None:
            worldtype = 0
        
        self.operator = OperateField(fieldtype, fieldsize)
        self.d = self.operator.d

    def get_map_raw(self) -> list:
        return self.operator.field

    def get_map_sendable(self) -> str:
        return self.operator.get_map_sendable(self.symbols)

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
        return fieldstr
    
    def add_player(self, ID:str, symbol:str) -> None:
        self.d[ID] = self.userNum + 11
        self.position[self.d[ID]] = self.operator.get_init_position()
        self.symbols[self.d[ID]] = symbol
        self.operator.paint_by_position(self.d[ID], self.position[self.d[ID]], 0)
        self.userNum += 1
    
    def get_user_position(self, ID:str) -> list:
        return self.position[self.d[ID]]    # [y, x]
    
    def overwrite_user_position(self, ID:str, position:list) -> None:
        self.position[self.d[ID]] = position
    
    def get_user_symbol(self, ID:str) -> str:
        return self.symbols[self.d[ID]]
    
    def overwrite_user_symbol(self, ID:str, symbol:str) -> None:
        self.symbols[self.d[ID]] = symbol
    
    def get_can_be_painted_direction(self, ID:str):
        return self.operator.can_be_painted(self.position[self.d[ID]])
    
    def paint_by_direction(self, ID:str, direction:str, item:int=0) -> int:
        pos = self.position[self.d[ID]]
        if direction == "w":
            pos[0] -= 1
        elif direction == "a":
            pos[1] -= 1
        elif direction == "d":
            pos[1] += 1
        elif direction == "s":
            pos[0] += 1
        else:
            # invalid direction charactor
            pass
        return self.operator.paint_by_position(self.d[ID], pos, item)
