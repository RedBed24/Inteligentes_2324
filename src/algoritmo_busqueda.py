from typing import Callable
from nodo import Nodo
from frontera import Frontera
from problema import Problema
from espacio_estados import Accion

def algoritmo_busqueda(problema : Problema, estrategia : Callable[[Nodo], float], heuristica : Callable[[Nodo, Problema], float], profundidad_maxima : int) -> list[Nodo]:
    # generados = sacados_frontera + frontera => frontera = generados - sacados_frontera
    # sacados_frontera = expandidos + solucion + previamente_visitados_cut
    # frontera y previamente_visitados_cut son derivados, no se cuentan
    SE_generados = 0
    SE_sacado_frontera = 0
    SE_expandido = 0
    SE_solucion = 0
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
        # si no es el primer nodo y es un nodo SE, se cuenta como sacado de frontera
        if nodo.accion and nodo.accion.direction == Accion.SOUTH_EAST:
            SE_sacado_frontera += 1
        if problema.objetivo(nodo.estado):
            if nodo.accion and nodo.accion.direction == Accion.SOUTH_EAST:
                SE_solucion += 1
            solucion = True
        elif nodo.estado not in visitados and nodo.profundidad < profundidad_maxima:
            if nodo.accion and nodo.accion.direction == Accion.SOUTH_EAST:
                SE_expandido += 1
            visitados.append(nodo.estado)  
            for sucesor in nodo.estado.sucessors():
                id_nodo += 1
                nuevo_nodo = Nodo(id_nodo, nodo, sucesor.to_state, nodo.profundidad + 1, nodo.costo_distancia + sucesor.length, max(nodo.costo_max_desnivel, sucesor.heigth_diff), 0, sucesor)
                nuevo_nodo.heuristica = heuristica(nuevo_nodo, problema)
                nuevo_nodo.valor = estrategia(nuevo_nodo)
                frontera.add(nuevo_nodo)
                # si es un nodo SE, se cuenta como generado
                if nuevo_nodo.accion.direction == Accion.SOUTH_EAST:
                    SE_generados += 1

    print(f"Nodos SE expandidos = {SE_expandido}")
    # generados = sacados_frontera + frontera => frontera = generados - sacados_frontera
    SE_en_frontera = SE_generados - SE_sacado_frontera
    print(f"Nodos SE en frontera = {SE_en_frontera}")

    # frontera - expandidos
    print(f"Nodos SE en frontera - expandidos = {SE_en_frontera - SE_expandido}")

    camino = []
    if solucion:
       camino = nodo.funcion_camino()

    return camino #si camino está vacío, es que no hay camino
