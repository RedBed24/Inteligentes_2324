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

def create_hdf5(filename : str, nodata_Value : float, sizeCell : float, submaps : list) -> None:
    with h5py.File(filename, "w") as f:
        for submap in submaps:
            # TODO: si no se guarda data, habría que leerla del fichero hdf5
            dataset = f.create_dataset(submap.name, data = submap.data)
            dataset.attrs["xinf"] = submap.inf.x
            dataset.attrs["yinf"] = submap.inf.y
            dataset.attrs["xsup"] = submap.sup.x
            dataset.attrs["ysup"] = submap.sup.y
            dataset.attrs["cellsize"] = sizeCell
            dataset.attrs["nodata_value"] = nodata_Value

def leer_dataset_hdf5(filename : str, dataset_name : str) -> list:
    data = None
    with h5py.File(filename, "r") as f:
        data = f[dataset_name][()]
    return data
