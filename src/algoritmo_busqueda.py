from nodo import Nodo
from frontera import Frontera
from espacio_estados import Estado 
from espacio_estados import Accion

# Definición de funciones (Provisional, además no debería ir aquí xd)
def anchura(nodo):
    return nodo.profundidad

def profundidad(nodo):
    return 1 / (nodo.profundidad + 1)

def costo_uniforme(nodo):
    return nodo.costo['distancia']

# Creación de un diccionario de funciones
diccionario_funciones = {
    'anchura': anchura,
    'profundidad': profundidad,
    'costo_uniforme': costo_uniforme
}

def algoritmo_busqueda(estado_inicial, estado_final, estrategia : function, cota : int):
    frontera = Frontera()
    visitados = []
    solucion = False
    nodo_inicial = Nodo(estado_inicial, 0, 0, 0, 0, 0, None, None)
    frontera.append(nodo_inicial)

    while (len(frontera) > 0 and not solucion):
        nodo=frontera.getNode()
        if nodo.estado == estado_final:
            solucion = True
        else:
            if (nodo.estado not in visitados and nodo.profundidad <= cota): 
                visitados.append(nodo.estado)  
                sucesores = nodo.estado.sucessor()
                for sucesor in sucesores:
                    nodo_añadir = Nodo(sucesor.to_state, 0, nodo.profundidad+1, nodo.costo['distancia'] + sucesor.length, max(nodo.costo['maxDesnivel'], sucesor.heigth), 0, sucesor, nodo.estado)
                    nodo_añadir.set_valor(estrategia)
                    frontera.add(nodo_añadir)


    camino = []
    if(solucion):
       camino = nodo.funcion_camino()

    return camino #si camino está vacío, es que no hay camino