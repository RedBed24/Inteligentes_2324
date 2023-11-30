from mapa import Mapa

import os.path
import json

def test_umt(mapa : Mapa, filename : str, roundval : int = 3) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()

        for line_num in range(len(lines)):
            y, x, value = lines[line_num][:-1].split("\t")

            y = int(y)
            x = int(x)

            value = float(value)
            val   = mapa.umt_YX(y, x)

            value = round(value, roundval)
            val   = round(val,   roundval)

            if val != value: print(f"{filename}:{line_num + 1}: {val}")
            assert val == value
    print(f"test {filename} passed")

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    test_umt(Mapa(os.path.join(config["data_folder"], config["mapa_hdf5"])), os.path.join("test_cases", "test_map_original.txt"))
    test_umt(Mapa(os.path.join(config["data_folder"], "300_mean.hdf5")), os.path.join("test_cases", "test_map_300_mean.txt"))
    test_umt(Mapa(os.path.join(config["data_folder"], "400_max.hdf5")), os.path.join("test_cases", "test_map_400_max.txt"))


if __name__ == "__main__":
    main()