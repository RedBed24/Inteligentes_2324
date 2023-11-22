from mapa import Mapa
import os.path
import json
import numpy as np

with open('config.json', 'r') as file:     config = json.load(file)

def test(filename : str, mapa : "Mapa", roundval = 3, do_round = False) -> None:
    count = 0
    count_error = 0

    error =  10 ** - roundval

    with open(filename, "r") as f:
        lines = f.readlines()

        for line_num in range(len(lines)):

            y, x, value = lines[line_num][:-1].split("\t")

            y = int(y)
            x = int(x)

            value = float(value)
            val   = mapa.umt_YX(y, x)

            if do_round:
                value = round(value, roundval)
                val   = round(val, roundval)

            if value != val:
                count += 1
                if abs(val - value) > error:
                    print(f"{line_num + 1:4d} {y:7} {x:6} {value:8.3f} {val:10.5f} {abs(val - value):.5f}")
                    count_error += 1

    return count, count_error, len(lines)


def main():
    DATAFOLDER = "data"
    # decimales que se redondean
    roundval = 0
    # redondear o no
    do_round = False

    map = Mapa(os.path.join(DATAFOLDER, "LaGomera.hdf5"))

    print(f"{'line':4} {'y':7} {'x':6} {'expeted':8} {'obtained':10} {'diff':5}")
    print(f"testing original")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_original.txt"), map, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")

    # leer si se existe else crear
    resized = Mapa(os.path.join(DATAFOLDER, "300_mean.hdf5")) if os.path.isfile(os.path.join(DATAFOLDER, "300_mean.hdf5")) else map.resize(300, np.mean, os.path.join(DATAFOLDER, "300_mean.hdf5"))
    print(f"testing map_300_mean")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_300_mean.txt"), resized, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")

    resized = Mapa(os.path.join(DATAFOLDER, "400_max.hdf5")) if os.path.isfile(os.path.join(DATAFOLDER, "400_max.hdf5")) else map.resize(400, max, os.path.join(DATAFOLDER, "400_max.hdf5"))
    print(f"testing map_400_max")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_400_max.txt"), resized, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")
    
    

if __name__ == "__main__":
    main()

