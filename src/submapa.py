from point import Point
import hdf5_data_handler as hdf5

class Submapa:
    def __init__(self, filename : str, path : str, inf : "Point", sup : "Point", sizeCell, nodata_Value : float) -> None:
        self.inf = inf
        self.sup = sup
        self.sizeCell = sizeCell
        self.nodata_Value = nodata_Value
        self.filename = filename
        self.path = path
        self.__data = None

    def data(self) -> list:
        # TODO: sólo se carga una vez, cuando se necesita por primera vez
        if self.__data is None:
            self.__data = hdf5.leer_dataset_hdf5(self.filename, self.path)
        return self.__data

    def __contains__(self, p : "Point") -> bool:
        return self.inf < p < self.sup
    
    def umt_YX(self, p : "Point") -> float:
        value = self.nodata_Value
        if p in self:
            # TODO: si no se guarda data, habría que leerla del fichero hdf5
            value = self.data()[int((p.y - self.yinf.y)/self.sizeCell)][int((p.x - self.inf.x)/self.sizeCell)]
        return value

    def resize(self, factor : int, transform : "function") -> "Submapa":
        new_data = []

        loaded_data = self.data()
        for i in range(0, len(loaded_data), factor):
            new_data.append([])
            for j in range(0, len(loaded_data[i]), factor):
                new_data[-1].append(transform(loaded_data[i:i+factor][j:j+factor]))

        return Submapa(self.inf, self.sup, new_data, self.sizeCell * factor, self.nodata_Value, self.name)

    def __str__(self) -> str:
        return f"({self.inf = }, {self.sup = }, {self.name = })"

    def __repr__(self) -> str:
        return self.__str__()

    def __gt__(self, other) -> bool:
        # FIXME: check x too
        return self.sup.y > other.sup.y

    def __ge__(self, other) -> bool:
        return self.sup.y >= other.sup.y

    def __lt__(self, other) -> bool:
        return self.sup.y < other.sup.y

    def __le__(self, other) -> bool:
        return self.sup.y <= other.sup.y

    def __eq__(self, other) -> bool:
        return self.sup.y == other.sup.y
