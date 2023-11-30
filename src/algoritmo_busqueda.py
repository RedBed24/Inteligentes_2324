from nodo import Nodo
from frontera import Frontera
from problema import Problema

def algoritmo_busqueda(problema : Problema, estrategia : "function", profundidad_maxima : int) -> list:
    id_nodo = 0
    frontera = Frontera()
    visitados = []
    solucion = False
    nodo_inicial = Nodo(id_nodo, None, problema.initial_state, 0, 0, 0, problema.heuristica(problema.initial_state), None)
    nodo_inicial.valor = estrategia(nodo_inicial)
    frontera.add(nodo_inicial)

    while len(frontera) and not solucion:
        nodo=frontera.getNode()
        if problema.objetivo(nodo.estado):
            solucion = True
        else:
            if nodo.estado not in visitados and nodo.profundidad <= cota: 
                visitados.append(nodo.estado)  
                for sucesor in nodo.estado.sucessor():
                    id_nodo += 1
                    nuevo_nodo = Nodo(id_nodo, nodo, sucesor.to_state, nodo.profundidad + 1, nodo.costo_distancia + sucesor.length, max(nodo.costo_max_desnivel, sucesor.heigth), problema.heuristica(sucesor.to_state), sucesor)
                    nuevo_nodo.valor = estrategia(nuevo_nodo)
                    frontera.add(nuevo_nodo)


    camino = []
    if solucion:
       camino = nodo.funcion_camino()

    return camino #si camino está vacío, es que no hay camino