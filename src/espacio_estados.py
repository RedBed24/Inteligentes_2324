import json
from mapa import Mapa
from point import Point

with open('config.json', 'r') as file:     config = json.load(file)

class Accion:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
    
    FACTOR = config["factor_desplazamiento"]
    ACCION_MAX_HEIGTH = config["accion_max_height"]

    def __init__(self, from_state , in_map : Mapa, direction) -> None:
        self.length = in_map.sizeCell * Accion.FACTOR
        self.direction = direction
        self.map = in_map

        match direction:
            case Accion.NORTH:
                self.to_state = Estado(from_state.p.y + self.length, from_state.p.x,self.map)
            case Accion.SOUTH:
                self.to_state = Estado(from_state.p.y - self.length, from_state.p.x,self.map)
            case Accion.EAST:
                self.to_state = Estado(from_state.p.y, from_state.p.x + self.length,self.map)
            case Accion.WEST:
                self.to_state = Estado(from_state.p.y, from_state.p.x - self.length,self.map)
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


class Estado:
    def __init__(self, y : float, x : float, in_map : Mapa) -> None:
        self.p = Point(x, y)
        self.id = f"({self.p.y},{self.p.x})"
        self.map = in_map
    
    def succesor(self) -> list:
        succesors = []
        for direction in Accion.DIRECTIONS:
            acc = Accion(self, self.map, direction)
            if acc.valid():
                succesors.append(acc)

        return succesors
    
    def __eq__(self, other : object) -> bool:
        return self.p == other.p
    
    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return self.__str__()