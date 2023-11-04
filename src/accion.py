from estado import Estado
from mapa import Mapa
import os
import json

with open('config.json', 'r') as file:     config = json.load(file)

class Accion:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
    
    FACTOR = config["factor_desplazamiento"]
    ACCION_MAX_HEIGTH = config["accion_max_heigth"]

    def __init__(self, from_state : Estado, in_map : Mapa, direction) -> None:
        self.length = in_map.sizeCell * Accion.FACTOR
        self.direction = direction
        self.map = in_map

        match direction:
            case Accion.NORTH:
                self.to_state = Estado(from_state.p.y + self.length, from_state.p.x)
            case Accion.SOUTH:
                self.to_state = Estado(from_state.p.y - self.length, from_state.p.x)
            case Accion.EAST:
                self.to_state = Estado(from_state.p.y, from_state.p.x + self.length)
            case Accion.WEST:
                self.to_state = Estado(from_state.p.y, from_state.p.x - self.length)
            case _:
                raise Exception(f"Invalid {direction = }")
        
        self.to_heigth = self.map.umt_Point(self.to_state.p)
        self.heigth = abs(self.to_heigth - self.map.umt_Point(from_state.p))
        

    def valid(self) -> bool:
        return self.to_heigth != self.map.nodata_Value and self.heigth <= Accion.ACCION_MAX_HEIGTH and self.to_state.p in self.map

    def __str__(self) -> str:
        return f"({self.direction}, {self.to_state}, ({self.length}, {self.heigth}))"
    
    def __repr__(self) -> str:
        return self.__str__()
