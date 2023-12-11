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

    factor = 250
    transform = np.mean
    map_name = os.path.join(config["data_folder"], "Gomerazoom250.hdf5")

    mp = Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"]))
    # Only need the file in disk, because Problema takes a path, not a Mapa
    _ = mp.resize(factor, transform, map_name)

    y0, x0 = (3118001, 271333)
    yf, xf = (3107001, 288833)

    Accion.ACCION_MAX_HEIGTH = 454
    Accion.FACTOR = 1

    maxdepth = 100000

    resultado = algoritmo_busqueda(
        Problema(map_name, y0, x0, yf, xf),
        estrategias.ASTAR,
        heuristicas.euclidean,
        maxdepth # prfundidad maxima
    )

    with open(os.path.join("resultados", "ejercicio1.txt"), "w") as f:
        f.write(f"file:ejercicio1\n")
        f.write(f"init:({y0}, {x0})\n")
        f.write(f"goal:({yf}, {xf})\n")
        f.write(f"strategy:BFS\n")
        f.write(f"maxdepth:{maxdepth}\n")
        for accion in resultado:
            f.write(f"{accion}\n")


if __name__ == "__main__":
    main()

