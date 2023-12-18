import math
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

    f=open("resultados/frontera.txt","w")
    while len(frontera) and not solucion:
        nodo = frontera.getNode()
        if problema.objetivo(nodo.estado):
            solucion = True
        elif nodo.estado not in visitados and nodo.profundidad < profundidad_maxima:
            visitados.append(nodo.estado)  
            for sucesor in nodo.estado.sucessors():
                if sucesor.direction == "N" or sucesor.direction == "S" or sucesor.direction == "E" or sucesor.direction == "W":
                    costeDistancia = nodo.costo_distancia + sucesor.length
                else:
                    costeDistancia = nodo.costo_distancia + sucesor.length * math.sqrt(2)
                id_nodo += 1
                nuevo_nodo = Nodo(id_nodo, nodo, sucesor.to_state, nodo.profundidad + 1,costeDistancia, max(nodo.costo_max_desnivel, sucesor.heigth_diff), 0, sucesor)
                nuevo_nodo.heuristica = heuristica(nuevo_nodo, problema)
                nuevo_nodo.valor = estrategia(nuevo_nodo)
                frontera.add(nuevo_nodo)
                f.write(f"{nuevo_nodo}\n")
                if nuevo_nodo.parent.estado.p.y==3108281 and nuevo_nodo.parent.estado.p.x==281933: print(nuevo_nodo.id) # Nodos con padre (3108281, 281933)

    camino = []
    if solucion:
       camino = nodo.funcion_camino()

    f.close()
    return camino #si camino está vacío, es que no hay camino




