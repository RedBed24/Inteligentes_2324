from __future__ import annotations
import json
from mapa import Mapa
from point import Point
from math import sqrt

with open('config.json', 'r') as file:     config = json.load(file)

class Accion:
    N = NORTH = "N"
    S = SOUTH = "S"
    E = EAST = "E"
    O = WEST = "O"
    NO = NORTH_WEST = "NO"
    NE = NORTH_EAST = "NE"
    SO = SOUTH_WEST = "SO"
    SE = SOUTH_EAST = "SE"
    DIRECTIONS =  [N,NE,E,SE,S,SO,O,NO]
    
    FACTOR = config["factor_desplazamiento"]
    ACCION_MAX_HEIGTH = config["accion_max_height"]
    
    @staticmethod
    def calculate_to_state(from_state : Estado, direction, length : float, map : Mapa) -> Estado:
        to_state = None
        match direction:
            case Accion.NORTH:
                to_state = Estado(from_state.p.y + length, from_state.p.x, map)
            case Accion.SOUTH:
                to_state = Estado(from_state.p.y - length, from_state.p.x, map)
            case Accion.EAST:
                to_state = Estado(from_state.p.y, from_state.p.x + length, map)
            case Accion.WEST:
                to_state = Estado(from_state.p.y, from_state.p.x - length, map)
            case Accion.NORTH_WEST:
                to_state = Estado(from_state.p.y + length, from_state.p.x - length, map)
            case Accion.NORTH_EAST:
                to_state = Estado(from_state.p.y + length, from_state.p.x + length, map)
            case Accion.SOUTH_WEST:
                to_state = Estado(from_state.p.y - length, from_state.p.x - length, map)
            case Accion.SOUTH_EAST:
                to_state = Estado(from_state.p.y - length, from_state.p.x + length, map)
            case _:
                raise Exception(f"Invalid {direction = }")
        return to_state
        

    def __init__(self, from_state : Estado, in_map : Mapa, direction):
        self.direction = direction
        self.length = in_map.sizeCell * Accion.FACTOR
        self.map = in_map

        self.to_state = Accion.calculate_to_state(from_state, direction, self.length, in_map)

        self.to_heigth = self.map.umt_Point(self.to_state.p)
        self.heigth_diff = abs(self.to_heigth - self.map.umt_Point(from_state.p))

        self.length = sqrt((self.to_state.p.x - from_state.p.x) ** 2 + (self.to_state.p.y - from_state.p.y) ** 2)


    def valid(self) -> bool:
        return self.to_heigth != self.map.nodata_Value and self.heigth_diff <= Accion.ACCION_MAX_HEIGTH

    def __str__(self) -> str:
        return f"('{self.direction}',{self.to_state},({float(self.length)},{round(self.heigth_diff, 3)}))"
    
    def __repr__(self) -> str:
        return self.__str__()


class Estado:
    def __init__(self, y : float, x : float, in_map : Mapa):
        self.p = Point(x, y)
        self.id = f"({int(self.p.y)},{int(self.p.x)})"
        self.map = in_map
    
    def sucessors(self) -> list[Accion]:
        sucessors = []
        for direction in Accion.DIRECTIONS:
            acc = Accion(self, self.map, direction)
            if acc.valid():
                sucessors.append(acc)

        return sucessors
    
    def __eq__(self, other : Estado) -> bool:
        return self.p == other.p
    
    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())
