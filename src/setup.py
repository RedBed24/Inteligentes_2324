import os.path
import json

import numpy as np
from problema import Problema
from mapa import Mapa
import estrategias
import heuristicas
from algoritmo_busqueda import algoritmo_busqueda

def main():
    with open('config.json', 'r') as file: config = json.load(file)
    os.makedirs("resultados", exist_ok=True)

    factor = 135
    transform = np.mean
    map_name = os.path.join(config["data_folder"], "Gomerazoom135.hdf5")

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    if not os.path.isfile(map_name):
        new = mp.resize(factor, transform, map_name)

    y0, x0 = 3115231, 270163
    yf, xf = 3110101, 292843

    maxdepth = 999999

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.ASTAR,
        heuristicas.euclidean, 
        maxdepth 
    )

    with open(os.path.join("resultados", "solucion.txt"), "w") as f:
        f.write(f"file:solucion.txt\n")
        f.write(f"init:({y0}, {x0})\n")
        f.write(f"goal:({yf}, {xf})\n")
        f.write(f"strategy:ASTAR\n") 
        f.write(f"maxdepth:{maxdepth}\n")
        for nodo in resultado:
            f.write(f"{nodo}\n")

if __name__ == "__main__":
    main()