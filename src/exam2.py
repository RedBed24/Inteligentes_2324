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

    factor = 280
    transform = np.max
    map_name = os.path.join(config["data_folder"], "Gomerazoom280.hdf5")

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    if not os.path.isfile(map_name):
        new = mp.resize(factor, transform, map_name)

    y0, x0 = 3117801, 270173
    yf, xf = 3108281, 290893

    maxdepth = 111

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.DFS,
        heuristicas.manhattan, 
        maxdepth 
    )

    with open(os.path.join("resultados", "solucion.txt"), "w") as f:
        f.write(f"file:solucion.txt")
        f.write(f"init:({y0}, {x0})")
        f.write(f"goal:({yf}, {xf})")
        f.write(f"strategy:DFS") 
        f.write(f"maxdepth:{maxdepth}")
        for nodo in resultado:
            f.write(f"{nodo}\n")

if __name__ == "__main__":
    main()