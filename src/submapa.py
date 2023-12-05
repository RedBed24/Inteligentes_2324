from __future__ import annotations
from typing import Callable
from point import Point
import numpy as np
import hdf5_data_handler as hdf5

class Submapa:
    def __init__(self, filename : str, path : str, inf : Point, sup : Point, sizeCell : int, nodata_Value : float, data : np.ndarray | None = None):
        self.inf = inf
        self.sup = sup
        self.sizeCell = sizeCell
        self.nodata_Value = nodata_Value
        self.filename = filename
        self.path = path
        self.__data = data

    def data(self) -> np.ndarray:
        if self.__data is None:
            self.__data = hdf5.leer_dataset_hdf5(self.filename, self.path)
        return self.__data

    def __contains__(self, p : Point) -> bool:
        return self.inf <= p < self.sup
    
    def umt_YX(self, p : Point) -> float:
        value = self.nodata_Value
        if p in self:
            col = int((self.sup.y - p.y) / self.sizeCell)
            row = int((p.x - self.inf.x) / self.sizeCell)
            value = self.data()[col][row]
        return value

    def resize(self, factor : int, transform : "function", nombre_nuevo : str) -> "Submapa":
        new_data = []

        loaded_data = self.data()
        for i in range(0, len(loaded_data), factor):
            new_data.append([])
            for j in range(0, len(loaded_data[i]), factor):
                end_row = min(i + factor , len(loaded_data))
                end_col = min(j + factor , len(loaded_data[i]))
                values = []
                for row in range(i, end_row):
                    for col in range(j, end_col):
                        if loaded_data[row][col] != self.nodata_Value:
                            values.append(loaded_data[row][col])
                new_data[-1].append(transform(values) if len(values) else self.nodata_Value)

        return Submapa(nombre_nuevo, self.path, self.inf, self.sup, self.sizeCell * factor, self.nodata_Value, data = np.array(new_data))

    def __str__(self) -> str:
        return f"({self.inf = }, {self.sup = }, {self.path = })"

    def __repr__(self) -> str:
        return self.__str__()

    def __gt__(self, other : Submapa) -> bool:
        return (self.sup.y, self.sup.x) > (other.sup.y, other.sup.x)

    def __ge__(self, other : Submapa) -> bool:
        return (self.sup.y, self.sup.x) >= (other.sup.y, other.sup.x)

    def __lt__(self, other : Submapa) -> bool:
        return (self.sup.y, self.sup.x) < (other.sup.y, other.sup.x)

    def __le__(self, other : Submapa) -> bool:
        return (self.sup.y, self.sup.x) <= (other.sup.y, other.sup.x)

    def __eq__(self, other : Submapa) -> bool:
        return (self.sup.y, self.sup.x) == (other.sup.y, other.sup.x)
