import unittest
import os
import json
from mapa import Mapa


with open('config.json', 'r') as file:
    config = json.load(file)

DATAFOLDER = config["data_folder"]

def comprobar_valores(test_case, valor_obtenido, valor_esperado, error):
    with test_case.subTest(a=valor_obtenido, b=valor_esperado, error=error):
        test_case.assertLessEqual(abs(valor_obtenido - valor_esperado), error)

class Test_T1(unittest.TestCase):
    
    def test_map(self):
        map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5"]))
        filename = os.path.join(DATAFOLDER, "test_map_original.txt")

        error = 0#10 ** -3

        with open(filename, "r") as f:
            lines = f.readlines()

            for line_num in range(len(lines)):
                y, x, value = lines[line_num][:-1].split("\t")
                y = int(y)
                x = int(x)

                value = float(value)
                val = map.umt_YX(y, x)

                value = round(value, 3)
                val = round(val, 3)

                comprobar_valores(self, val, value, error)

    def test_map_300(self):
        map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5_300"]))
        filename = os.path.join(DATAFOLDER, "test_map_300_mean.txt")

        error = 0#10 ** -3

        with open(filename, "r") as f:
            lines = f.readlines()

            for line_num in range(len(lines)):
                y, x, value = lines[line_num][:-1].split("\t")
                y = int(y)
                x = int(x)

                value = float(value)
                val = map.umt_YX(y, x)

                value = round(value, 3)
                val = round(val, 3)

                comprobar_valores(self, val, value, error)

    def test_map_400(self):
            map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5_400"]))
            filename = os.path.join(DATAFOLDER, "test_map_400_max.txt")

            error = 0#10 ** -3

            with open(filename, "r") as f:
                lines = f.readlines()

                for line_num in range(len(lines)):
                    y, x, value = lines[line_num][:-1].split("\t")
                    y = int(y)
                    x = int(x)

                    value = float(value)
                    val = map.umt_YX(y, x)

                    value = round(value, 3)
                    val = round(val, 3)

                    comprobar_valores(self, val, value, error)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Tests finalizados")
