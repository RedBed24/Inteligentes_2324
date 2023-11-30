from __future__ import annotations
from espacio_estados import Accion, Estado

class Nodo:
    def __init__(self, id : int, parent : Nodo | None, estado : Estado, profundidad : int, costo_distancia : float, costo_max_desnivel : float, heuristica : float, accion : Accion | None):
        self.id = id
        self.parent = parent
        self.estado = estado
        self.valor : float
        self.profundidad = profundidad
        self.costo_distancia = costo_distancia
        self.costo_max_desnivel = costo_max_desnivel
        self.heuristica = heuristica
        self.accion = accion

    def __str__(self) -> str:
        id_parent = self.parent.id if self.parent is not None else None
        direction = self.accion.direction if self.accion is not None else None
        return f"[{self.id}][({round(self.costo_distancia, 3)},{round(self.costo_max_desnivel, 3)}),{self.estado.id},{id_parent},{direction},{self.profundidad},{self.heuristica},{round(self.valor, 3)}]"
    
    def __repr__(self) -> str:
        return self.__str__()   
    
    def funcion_camino(self) -> list[Nodo]:
        camino = [self]

        if self.parent is not None:
            camino = self.parent.funcion_camino() + camino
        
        return camino
    
    def __eq__(self, other : Nodo) -> bool:
        return (self.valor, self.id) == (other.valor, other.id)

    def __lt__(self, other : Nodo) -> bool:
        return (self.valor, self.id) < (other.valor, other.id)

    def __le__(self, other : Nodo) -> bool:
        return (self.valor, self.id) <= (other.valor, other.id)
    
    def __gt__(self, other : Nodo) -> bool:
        return (self.valor, self.id) > (other.valor, other.id)

    def __ge__(self, other : Nodo) -> bool:
        return (self.valor, self.id) >= (other.valor, other.id)


