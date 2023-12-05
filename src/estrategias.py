from nodo import Nodo

def BFS(nodo : Nodo) -> float:
    return nodo.profundidad

def DFS(nodo : Nodo) -> float:
    return 1 / (1 + nodo.profundidad)

def UCS(nodo : Nodo) -> float:
    return nodo.costo_distancia
