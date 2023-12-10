from typing import Callable
from nodo import Nodo
from frontera import Frontera
from problema import Problema

def algoritmo_busqueda(problema : Problema, estrategia : Callable[[Nodo], float], heuristica : Callable[[Nodo, Problema], float], profundidad_maxima : int) -> list[Nodo]:
    id_nodo = 0
    frontera = Frontera()
    visitados = []
    solucion = False
    nodo = Nodo(id_nodo, None, problema.initial_state, 0, 0, 0, 0, None)
    nodo.heuristica = heuristica(nodo, problema)
    nodo.valor = estrategia(nodo)
    frontera.add(nodo)

    while len(frontera) and not solucion:
        nodo = frontera.getNode()
        if problema.objetivo(nodo.estado):
            solucion = True
        elif nodo.estado not in visitados and nodo.profundidad <= profundidad_maxima:
            visitados.append(nodo.estado)  
            for sucesor in nodo.estado.sucessors():
                id_nodo += 1
                nuevo_nodo = Nodo(id_nodo, nodo, sucesor.to_state, nodo.profundidad + 1, nodo.costo_distancia + sucesor.length, max(nodo.costo_max_desnivel, sucesor.heigth_diff), 0, sucesor)
                nuevo_nodo.heuristica = heuristica(nuevo_nodo, problema)
                nuevo_nodo.valor = estrategia(nuevo_nodo)
                frontera.add(nuevo_nodo)

    camino = []
    if solucion:
       camino = nodo.funcion_camino()

    return camino #si camino está vacío, es que no hay camino
