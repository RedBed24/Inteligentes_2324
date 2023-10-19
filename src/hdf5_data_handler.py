import h5py

from submapa import Submapa
from point import Point

def leer_hdf5(filename : str) -> tuple:
    maps = []
    nodata_Value = 0
    sizeCell = 0

    with h5py.File(filename, "r") as f:
        for key in f.keys():
            dataset = f[key]

            inf = Point(dataset.attrs["xinf"], dataset.attrs["yinf"])
            sup = Point(dataset.attrs["xsup"], dataset.attrs["ysup"])
            sizeCell = dataset.attrs["cellsize"]
            nodata_Value = dataset.attrs["nodata_value"]

            maps.append(Submapa(filename, key, inf, sup, sizeCell, nodata_Value))

    return f, nodata_Value, sizeCell, maps

def create_hdf5(filename : str, new_submaps : list) -> None:
    with h5py.File(filename, "w") as f:
        for new_submap in new_submaps:
            dataset = f.create_dataset(new_submap.name, data = new_submap.data())
            dataset.attrs["xinf"] = new_submap.inf.x
            dataset.attrs["yinf"] = new_submap.inf.y
            dataset.attrs["xsup"] = new_submap.sup.x
            dataset.attrs["ysup"] = new_submap.sup.y
            dataset.attrs["cellsize"] = new_submap.sizeCell
            dataset.attrs["nodata_value"] = new_submap.nodata_Value

def leer_dataset_hdf5(filename : str, dataset_name : str) -> list:
    data = None
    with h5py.File(filename, "r") as f:
        data = f[dataset_name][()]
    return data
