from point import Point
from accion import Accion
from mapa import Mapa

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
