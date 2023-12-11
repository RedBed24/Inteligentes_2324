from mapa import Mapa
import hdf5_data_handler as hdf5
import numpy as np
import os.path
import json
from algoritmo_busqueda import algoritmo_busqueda
from problema import Problema
import estrategias
import heuristicas

def set_up_maps(map, config):
    '''
    Construir el mapa Gomerazoom200.hdf5 a partir del mapa original LaGomera.hdf5 aplicando un resize de 200 
    con la operación media.Resolver, sobre el mapa obtenido, el problema de ir del punto geográfico (3111801, 269933) 
    al punto (3113801, 291933) mediante un paso de tamaño 1,usando la estrategia Profundidad con profundidad máxima 180 y
    la heurística de la distancia euclídea. Las acciones válidas son [N,E,SE,S,O,NO] 
    siempre que se verifique que desnivel sea menor o igual a 456.
    '''

    factor =200
    transform = np.mean
    map_name = config["maps_names"]["200_mean"]

    mapa=map.resize(factor, transform, os.path.join(config["data_folder"], map_name))

    #hdf5.create_hdf5(os.path.join(config["data_folder"], map_name), mapa.submaps)

    y0, x0 = 3111801, 269933
    yf, xf = 3113801, 291933

    maxdepth = 180

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.DFS,
        heuristicas.euclidean, # heurística, cambiar por heuristicas.manhattan
        maxdepth # prfundidad maxima
    )

    with open(os.path.join("resultados", "ejercicio1.txt"), "b") as f:
        f.write(f"file:ejercicio1")
        f.write(f"init:({y0}, {x0})")
        f.write(f"goal:({yf}, {xf})")
        f.write(f"strategy:DFS")
        f.write(f"maxdepth:{maxdepth}")
        for accion in resultado:
            f.write(f"{accion}\n")


def main():
    with open('config.json', 'r') as file: config = json.load(file)

    set_up_maps(Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"])), config)

if __name__ == "__main__":
    main()
