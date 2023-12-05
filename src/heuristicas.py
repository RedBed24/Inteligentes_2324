from nodo import Nodo
from problema import Problema

from math import sqrt

def euclidean(nodo : Nodo, problema : Problema) -> float:
    return sqrt((problema.end_state.p.x - nodo.estado.p.x) ** 2 + (problema.end_state.p.y - nodo.estado.p.y) ** 2)

def manhattan(nodo : Nodo, problema : Problema) -> float:
    return abs(problema.end_state.p.x - nodo.estado.p.x) + abs(problema.end_state.p.y - nodo.estado.p.y)
