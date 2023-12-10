from mapa import Mapa

import numpy as np
import os.path
import json

def set_up_maps(map, config):
    factor = 300
    transform = np.mean
    map_name = config["maps_names"]["300_mean"]

    map.resize(factor, transform, os.path.join(config["data_folder"], map_name))

    factor = 400
    transform = np.max
    map_name = config["maps_names"]["400_max"]

    map.resize(factor, transform, os.path.join(config["data_folder"], map_name))

def main():
    with open('config.json', 'r') as file: config = json.load(file)

    set_up_maps(Mapa(os.path.join(config["data_folder"], config["maps_names"]["original"])), config)

if __name__ == "__main__":
    main()
