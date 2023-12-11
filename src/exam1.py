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

    factor = 275
    transform = np.mean
    map_name = "Gomerazoom275"

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    new = mp.resize(factor, transform, map_name)

    y0, x0 = 3116901, 270583
    yf, xf = 3108651, 290383

    maxdepth = 108

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.DFS,
        heuristicas.euclidean, # heurística
        maxdepth # prfundidad maxima
    )

    with open(os.path.join("resultados", "ejercicio1.txt"), "w") as f:
        f.write(f"file:ejercicio1")
        f.write(f"init:({y0}, {x0})")
        f.write(f"goal:({yf}, {xf})")
        f.write(f"strategy:DFS")
        f.write(f"maxdepth:{maxdepth}")
        for accion in resultado:
            f.write(f"{accion}\n")

if __name__ == "__main__":
    main()


