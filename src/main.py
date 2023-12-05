from mapa import Mapa

import numpy as np
import os.path
import json

def set_up_maps(map, config):
    factor = 300
    transform = np.mean
    map_name = "GomeraZoom300.hdf5"

    map.resize(factor, transform, os.path.join(config["data_folder"], map_name))

    factor = 400
    transform = np.max
    map_name = "400_max.hdf5"

    map.resize(factor, transform, os.path.join(config["data_folder"], map_name))

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    set_up_maps(Mapa(os.path.join(config["data_folder"], config["mapa_hdf5"])), config)

if __name__ == "__main__":
    main()
