import os.path
import json
import unittest
import re

import estrategias
import heuristicas
from mapa import Mapa
from problema import Problema
from algoritmo_busqueda import algoritmo_busqueda

from test_T2 import Create_From_String

ALGORITMOS = {
    "BFS": estrategias.BFS,
    "DFS": estrategias.DFS,
    "UCS": estrategias.UCS
}

with open('config.json', 'r') as file:
    config = json.load(file)

def redondear_lista(lista):
    resultado = []

    for elemento in lista:
        parte_decimal = elemento % 1

        if parte_decimal < 0.5:
            # Redondear hacia abajo
            redondeado = round(elemento)
        else:
            # Redondear hacia arriba
            redondeado = round(elemento) + 1

        resultado.append(redondeado)

    return resultado

def normalizar_valores(cadena):
    # Encuentra todos los números en la cadena
    numeros = re.findall(r"[-+]?\d*\.\d+|\d+", cadena)
    # Convierte los números a punto flotante
    numeros_float = [float(num) for num in numeros]
    numeros_redondeados=redondear_lista(numeros_float)
    return numeros_redondeados

def comprobar_valores(test_case, esperado, resultado):
    esperado = normalizar_valores(esperado)
    resultado = normalizar_valores(resultado)
    with test_case.subTest(a=esperado, b=resultado):
        assert esperado == resultado

def run_test_case(test_case, path):
    with open(path, "r") as f:
        lines = f.readlines()

        file = os.path.join(config["data_folder"], lines.pop(0)[:-1].split(":")[1]) # EL NOMBRE NO COINCIDE CON NUESTRO HDF5 DE 300X300
        file = os.path.join(config["data_folder"], config["mapa_hdf5_300"])
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

        resultado = algoritmo_busqueda(problema, strategy,heuristica, profundidad_maxima) # FALTA AÑADIR LA HEURISTICA
        for line_num in range(len(lines)):
            comprobar_valores(test_case, lines[line_num][:-1], str(resultado[line_num]))

class Test_T3(unittest.TestCase):

    def test_example1(self):
        dir = os.path.join("test_cases", "ejemplo")
        path = os.path.join(dir, "ejemplo1.txt")
        run_test_case(self, path)

    def test_example2(self):
        dir = os.path.join("test_cases", "ejemplo")
        path = os.path.join(dir, "ejemplo2.txt")
        run_test_case(self, path)

    def test_example3(self):
        dir = os.path.join("test_cases", "ejemplo")
        path = os.path.join(dir, "ejemplo3.txt")
        run_test_case(self, path)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Tests finalizados")