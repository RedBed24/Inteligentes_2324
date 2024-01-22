from typing import Callable
from nodo import Nodo
from frontera import Frontera
from problema import Problema
from espacio_estados import Accion

def algoritmo_busqueda(problema : Problema, estrategia : Callable[[Nodo], float], heuristica : Callable[[Nodo, Problema], float], profundidad_maxima : int) -> list[Nodo]:
    id_nodo = 0
    frontera = Frontera()
    visitados = []
    solucion = False
    nodo = Nodo(id_nodo, None, problema.initial_state, 0, 0, 0, 0, None)
    nodo.heuristica = heuristica(nodo, problema)
    nodo.valor = estrategia(nodo)
    frontera.add(nodo)
    nodos_este_expandidos=0 # AÑADE PARA RESOLUCIÓN EXAMEN ORDINARIO
    nodos_este_sacados_frontera=0 # AÑADE PARA RESOLUCIÓN EXAMEN ORDINARIO
    while len(frontera) and not solucion:
        nodo = frontera.getNode()
        if nodo.accion is not None and nodo.accion.direction == Accion.EAST:
            nodos_este_sacados_frontera = nodos_este_sacados_frontera+1 # AÑADE PARA RESOLUCIÓN EXAMEN ORDINARIO
        #if nodo.estado.p.y == 3108281 and nodo.estado.p.x == 281933 : #El id del último nodo que visito el estado (3108281, 281933) es 
        #    print(nodo.id)
        # if nodo.estado.parent.parent is not None and nodo.estado.parent.parent.p.y == 3108281 and nodo.estado.parent.parent.p.x == 281933 : #El id del nodo cuyo abuelo visito el estado (3108281, 281933)
        #    print(nodo.id)
        if problema.objetivo(nodo.estado):
            solucion = True
        elif nodo.estado not in visitados and nodo.profundidad < profundidad_maxima:
            visitados.append(nodo.estado)  
            for sucesor in nodo.estado.sucessors():
                id_nodo += 1
                nuevo_nodo = Nodo(id_nodo, nodo, sucesor.to_state, nodo.profundidad + 1, nodo.costo_distancia + sucesor.length, max(nodo.costo_max_desnivel, sucesor.heigth_diff), 0, sucesor)
                nuevo_nodo.heuristica = heuristica(nuevo_nodo, problema)
                nuevo_nodo.valor = estrategia(nuevo_nodo)
                frontera.add(nuevo_nodo)
                if(sucesor.direction==Accion.EAST):
                    nodos_este_expandidos=nodos_este_expandidos+1 # AÑADE PARA RESOLUCIÓN EXAMEN ORDINARIO

    print(f"nodos expandidos: {nodos_este_expandidos}, nodos sacados: {nodos_este_sacados_frontera}, nodos que se han quedado en la frontera: {nodos_este_expandidos-nodos_este_sacados_frontera}") # AÑADE PARA RESOLUCIÓN EXAMEN ORDINARIO
    camino = []
    if solucion:
       camino = nodo.funcion_camino()

    return camino #si camino está vacío, es que no hay camino
