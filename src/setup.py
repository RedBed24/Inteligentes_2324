from mapa import Mapa

import numpy as np
import os.path
import json
import estrategias
from algoritmo_busqueda import algoritmo_busqueda
from problema import Problema
import heuristicas

def main():
    with open('config.json', 'r') as file: config = json.load(file)
    os.makedirs("resultados", exist_ok=True)

    factor = 280
    transform = max
    map_name = os.path.join(config["data_folder"], "Gomerazoom280.hdf5")

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    if not os.path.isfile(map_name):
        new = mp.resize(factor, transform, map_name)

    y0, x0 = 3117801, 270173
    yf, xf = 3108281, 290893

    maxdepth = 111

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.GREEDY,
        heuristicas.manhattan,
        maxdepth # prfundidad maxima
    )

    with open(os.path.join("resultados", "solucion.txt"), "w") as f:
        f.write(f"file:solucion.txt\n")
        f.write(f"init:({y0}, {x0})\n")
        f.write(f"goal:({yf}, {xf})\n")
        f.write(f"strategy:VORAZ\n") 
        f.write(f"maxdepth:{maxdepth}\n")
        for nodo in resultado:
            f.write(f"{nodo}\n")

if __name__ == "__main__":
    main()


