import unittest
import os
import json
from mapa import Mapa
from espacio_estados import Estado

with open('config.json', 'r') as file:
    config = json.load(file)

DATAFOLDER = config["data_folder"]

def Create_From_String(string : str, in_map : Mapa) -> Estado:
        y, x = string[1:-1].split(',')
        return Estado(float(y), float(x), in_map)

def comprobar_valores(test_case,succ,divisiones):
    with  test_case.subTest(a=succ, b=divisiones):
        assert succ == divisiones

class Test_T2(unittest.TestCase):

    def test_map_300(self):
         
        map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5_300"]))
        filename = os.path.join(DATAFOLDER, "sucesores_300_mean.txt")

        with open(filename, "r") as f:
            lines = f.readlines()
            for line_num in range(len(lines)):
                divisiones = lines[line_num][:-1].split("\t")
                estado = Create_From_String(divisiones.pop(0), map)
                succ = [str(acc) for acc in estado.sucessors()]                        
                comprobar_valores(self,succ,divisiones)

    def test_map_400(self):
         
        map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5_400"]))
        filename = os.path.join(DATAFOLDER, "sucesores_400_max.txt")

        with open(filename, "r") as f:
            lines = f.readlines()
            for line_num in range(len(lines)):
                divisiones = lines[line_num][:-1].split("\t")
                estado = Create_From_String(divisiones.pop(0), map)
                succ = [str(acc) for acc in estado.sucessors()]
                comprobar_valores(self,succ,divisiones)
        
if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        print("Tests finalizados")
        