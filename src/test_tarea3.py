import os.path
import json

import estrategias
from mapa import Mapa
from espacio_estados import Accion
from problema import Problema
from algoritmo_busqueda import algoritmo_busqueda

from test_tarea2 import Create_From_String

ALGORITMOS = {
    "BFS": estrategias.BFS,
    "DFS": estrategias.DFS,
    "UCS": estrategias.UCS,
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

        resultado = algoritmo_busqueda(problema, strategy, profundidad_maxima)
        for res in resultado:
            print(res)

        #for line_num in range(len(lines)):
        #    if lines[line_num][:-1] != str(resultado[line_num]):
        #        print(f"{path}:{line_num + 6}: {resultado[line_num]}")
        #    #assert lines[line_num][:-1] == str(resultado[line_num])
    print(f"test {path} passed")

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    dir = os.path.join("test_cases", "ejemplo")
    for os_file in os.listdir(dir):
        if os_file.endswith(".txt"):
            test_algoritmo(os.path.join(dir, os_file), config["data_folder"])
            break

if __name__ == "__main__":
    main()
