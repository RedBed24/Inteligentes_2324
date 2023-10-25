import hdf5_data_handler as hdf5
from point import Point

class Mapa:
    def __init__(self, filename : str) -> None:
        self.filename = filename
        self.f, self.submaps = hdf5.leer_hdf5(self.filename)

        self.submaps.sort(reverse = True)

        self.nodata_Value = self.submaps[0].nodata_Value
        self.sizeCell = self.submaps[0].sizeCell

        self.upLeft, self.downRight = self.__calc_corners()

        self.dim = [(self.downRight.x - self.upLeft.x) / self.sizeCell, (self.upLeft.y - self.downRight.y) / self.sizeCell]

    def __calc_corners(self) -> tuple:
        lowest = Point(self.submaps[0].inf.y, self.submaps[0].inf.x)
        highest = Point(self.submaps[0].sup.y, self.submaps[0].sup.x)

        for submap in self.submaps[1:]:
            # nos quedamos con la coordenada x e y más bajas
            if submap.inf.y < lowest.y:
                lowest.y = submap.inf.y
            if submap.inf.x < lowest.x:
                lowest.x = submap.inf.x

            # nos quedamos con la coordenada x e y más altas
            if submap.sup.y > highest.y:
                highest.y = submap.sup.y
            if submap.sup.x > highest.x:
                highest.x = submap.sup.x

        return Point(lowest.x, highest.y), Point(highest.x, lowest.y)
    
    def umt_YX(self, y : float, x : float) -> float:
        """Dadas las coordenadas Y-UMT y X-UMT debe devolver el valor correspondiente a la celda del grid que corresponda a la posición de dichas coordenadas. Si no existe valor en dichas coordenadas devolverá el valor Mapa.nodata_Value."""
        return self.umt_Point(Point(x, y))

    def umt_Point(self, p : "Point") -> float:
        """Dadas las coordenadas Y-UMT y X-UMT debe devolver el valor correspondiente a la celda del grid que corresponda a la posición de dichas coordenadas. Si no existe valor en dichas coordenadas devolverá el valor Mapa.nodata_Value."""
        if p in self:
            for submap in self.submaps:
                if p in submap:
                    return submap.umt_YX(p)
        return self.nodata_Value

    def resize(self, factor : int, transform : "function", nombre_nuevo : str) -> "Mapa":
        new_submaps = []
        for submap in self.submaps:
            new_submaps.append(submap.resize(factor, transform))
        
        hdf5.create_hdf5(nombre_nuevo, new_submaps)
        
        return Mapa(nombre_nuevo)

    def __str__(self) -> str:
        return f"({self.filename = }, {self.nodata_Value = }, {self.sizeCell = }, {self.dim = }, {self.upLeft = }, {self.downRight = })"
    
    def __repr__(self) -> str:
        return self.__str__()

    def __contains__(self, p : "Point") -> bool:
        return Point(self.upLeft.x, self.downRight.y) < p < Point(self.downRight.x, self.upLeft.y)
