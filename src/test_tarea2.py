from mapa import Mapa
from espacio_estados import Estado

import json
import os.path

def Create_From_String(string : str, in_map : Mapa) -> Estado:
        y, x = string[1:-1].split(',')
        return Estado(int(y), int(x), in_map)

def test_2(map, filename) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()
        for line_num in range(len(lines)):
            divisiones = lines[line_num][:-1].split("\t")
            estado = Create_From_String(divisiones.pop(0), map)
            succ = [str(acc) for acc in estado.sucessors()]

            if succ != divisiones:
                print(f"{filename}:{line_num + 1}: {succ}")
                print(divisiones)
            assert succ == divisiones
    print(f"test {filename} passed")

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    test_2(Mapa(os.path.join(config["data_dir"], "400_max.hdf5")), os.path.join("test_cases", "sucesores_400_max.txt"))
    test_2(Mapa(os.path.join(config["data_dir"], "300_mean.hdf5")), os.path.join("test_cases", "sucesores_300_mean.txt"))

if __name__ == "__main__":
    main()
