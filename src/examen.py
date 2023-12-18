import os.path
import json
import numpy as np

from problema import Problema
from mapa import Mapa
import estrategias
import heuristicas
from algoritmo_busqueda import algoritmo_busqueda
from espacio_estados import Accion

def main():
    with open('config.json', 'r') as file: config = json.load(file)
    os.makedirs("resultados", exist_ok=True)

    factor = 280
    transform = max
    nombre = "Gomerazoom280.hdf5"
    map_name = os.path.join(config["data_folder"], nombre)

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    # Only need the file in disk, because Problema takes a path, not a Mapa
    _ = mp.resize(factor, transform, map_name)

    y0, x0 = (3105481, 274093)
    yf, xf = (3120601, 284733)

    Accion.ACCION_MAX_HEIGTH = 595
    Accion.FACTOR = 1

    maxdepth = 81

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.GREEDY,
        heuristicas.manhattan,
        maxdepth # prfundidad maxima
    )

    with open(os.path.join("resultados", "solution.txt"), "w") as f:
        f.write(f"file:{nombre}\n")
        f.write(f"init:({y0}, {x0})\n")
        f.write(f"goal:({yf}, {xf})\n")
        f.write(f"strategy:BFS\n")
        f.write(f"maxdepth:{maxdepth}\n")
        for accion in resultado:
            f.write(f"{accion}\n")


if __name__ == "__main__":
    main()

