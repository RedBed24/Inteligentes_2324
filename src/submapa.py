from point import Point

class Submapa:
    def __init__(self, inf : "Point", sup : "Point", data, sizeCell, nodata_Value, name) -> None:
        # TODO: si se quiere no guardar datos en ram, se debe guardar una referencia al fichero hdf5
        self.inf = inf
        self.sup = sup
        self.data = data
        self.sizeCell = sizeCell
        self.nodata_Value = nodata_Value
        self.name = name

    def __contains__(self, p : "Point") -> bool:
        return self.inf < p < self.sup
    
    def umt_YX(self, p : "Point") -> float:
        value = self.nodata_Value
        if p in self:
            # TODO: si no se guarda data, habría que leerla del fichero hdf5
            value = self.data[int((p.y - self.yinf.y)/self.sizeCell)][int((p.x - self.inf.x)/self.sizeCell)]
        return value

    def resize(self, factor : int, transform : "function") -> "Submapa":
        new_data = []

        # TODO: si no se guarda data, habría que leerla del fichero hdf5
        for i in range(0, len(self.data), factor):
            new_data.append([])
            for j in range(0, len(self.data[i]), factor):
                new_data[-1].append(transform(self.data[i:i+factor][j:j+factor]))

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
