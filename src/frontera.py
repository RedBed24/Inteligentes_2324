from espacio_estados import Accion,Estado
from nodo import Nodo
from bisect import insort

class Frontera:
    def __init__(self) -> None:
        self.frontera = []

    # Insertar de forma ordenada elementos a la frontera
    def add(self, nodo : Nodo) -> None:
        insort(self.frontera, nodo)

    # Obtener el tamaño de la frontera
    def len(self) -> int:
        return len(self.frontera)
    
    # Obtener nodo de la frontera
    def getNode(self)-> Nodo:
        return self.frontera.pop(0) if self.len() > 0 else None
