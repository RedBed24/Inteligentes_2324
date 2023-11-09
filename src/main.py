from mapa import Mapa
from espacio_estados import Accion,Estado
from nodo import Nodo
from frontera import Frontera
import os.path
import json

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

def test_espacio_estados_y_frontera(map:Mapa):
    # NODOS Y FRONTERAS
    estado1 = Estado(1, 1, map)
    estado2 = Estado(1, 2, map)
    estado3 = Estado(1, 3, map)

    accion1= Accion(from_state=estado1, in_map=map,direction="N")
    accion2= Accion(from_state=estado2,in_map= map, direction="N")
    accion3= Accion(from_state=estado3,in_map= map, direction="N")


    nodo1 = Nodo(estado1, 0, 0, 1, 1,accion1, None)
    nodo2 = Nodo(estado2, 1, 1, 1, 1,accion2, nodo1)
    nodo3 = Nodo(estado3, 1, 1, 1, 1,accion3, nodo1)
    nodo4 = Nodo(estado2, 2, 2, 1, 1,accion2,nodo2)
    nodo5 = Nodo(estado3, 2, 2, 1, 1,accion3,nodo2)
    nodo6 = Nodo(estado3, 2, 2, 1, 1,accion3,nodo2)
    nodo7 = Nodo(estado3, 2, 2, 1, 1,accion3,nodo3)

    frontera=Frontera()
    frontera.add(nodo1)
    frontera.add(nodo2)
    frontera.add(nodo3)
    frontera.add(nodo4)
    frontera.add(nodo5)
    frontera.add(nodo6)
    frontera.add(nodo7)

    print("FRONTERA")
    print(frontera.len())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())
    print(frontera.getNode())


def main():
    DATAFOLDER = config["datafolder"]
    # decimales que se redondean
    roundval = 0
    # redondear o no
    do_round = False

    map = Mapa(os.path.join(DATAFOLDER, config["mapa_hdf5"]))
    print(f"{'line':4} {'y':7} {'x':6} {'expeted':8} {'obtained':10} {'diff':5}")
    print(f"testing original")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_original.txt"), map, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")


    mean = lambda x: round(sum(x) / len(x), 3) # redondea la media a 3 decimales
    # leer si se existe else crear
    resized = Mapa(os.path.join(DATAFOLDER, "300_mean.hdf5")) if os.path.isfile(os.path.join(DATAFOLDER, "300_mean.hdf5")) else map.resize(300, mean, os.path.join(DATAFOLDER, "300_mean.hdf5"))
    print(f"testing map_300_mean")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_300_mean.txt"), resized, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")

    resized = Mapa(os.path.join(DATAFOLDER, "400_max.hdf5")) if os.path.isfile(os.path.join(DATAFOLDER, "400_max.hdf5")) else map.resize(400, max, os.path.join(DATAFOLDER, "400_max.hdf5"))
    print(f"testing map_400_max")
    count, count_error, lenlines = test(os.path.join(DATAFOLDER, "test_map_400_max.txt"), resized, roundval, do_round)
    print(f"Out of {lenlines}, {count}({count/lenlines * 100:.2f}%) fails, {count_error}({count_error/count * 100:.2f}% error/fail, {count_error/lenlines * 100:.2f}% error/total) with distance > {10 ** - roundval}" if count != 0 else "No errors")
    
    test_espacio_estados_y_frontera(map)


if __name__ == "__main__":
    main()
