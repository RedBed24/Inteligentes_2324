import os.path
import json

from espacio_estados import Accion
import estrategias
import heuristicas
from mapa import Mapa
from problema import Problema
from algoritmo_busqueda import algoritmo_busqueda

from test_tarea2 import Create_From_String

ALGORITMOS = {
    "BFS": estrategias.BFS,
    "DFS": estrategias.DFS,
    "UCS": estrategias.UCS,
    "GREEDY": estrategias.GREEDY,
    "A*": estrategias.ASTAR,
}

def test_algoritmo(path, maps_dir):
    with open(path, "r") as f:
        lines = f.readlines()

        file = os.path.join(maps_dir, lines.pop(0)[:-1].split(":")[1])
        init = Create_From_String(lines.pop(0)[:-1].split(":")[1], Mapa(file))
        goal = Create_From_String(lines.pop(0)[:-1].split(":")[1], Mapa(file))
        strategy = ALGORITMOS[lines.pop(0)[:-1].split(":")[1]]
        profundidad_maxima = int(lines.pop(0)[:-1].split(":")[1])

        problema = Problema(file, init.p.y, init.p.x, goal.p.y, goal.p.x)

        heuristica = lambda x, y: 0.0
        if "euclidea" in path:
            heuristica = heuristicas.euclidean
        elif "manhattan" in path:
            heuristica = heuristicas.manhattan

        resultado = algoritmo_busqueda(problema, strategy, heuristica, profundidad_maxima)

        for i in range(len(resultado)):
            assert lines[i][:-1] == str(resultado[i])

    print(f"test {path} passed")

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    Accion.ACCION_MAX_HEIGTH = 100

    for tarea in ["T3", "T4"]:
        dir = os.path.join(config["test_folders"]["base"], config["test_folders"][tarea])
        for os_file in os.listdir(dir):
            if os_file.endswith(".txt"):
                test_algoritmo(os.path.join(dir, os_file), config["data_folder"])

if __name__ == "__main__":
    main()
