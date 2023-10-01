# TODO: Implementar la clase Mapa
class Mapa:
    def __init__(self, filename : str) -> None:
        self.nodata_Value# float. Valor para las celdas del grid que no contienen un valor válido. Si el mapa tiene más de un dataset este valor debe ser igual para todos.
        self.sizeCell# float. Tamaño en metros de un lado de la celda de un dataset. Si existen varios datasets este valor debe ser similar en todos.
        self.upLeft# (max_Y:float,min_X:float). Par de coordenadas Y-UMT, X-UMT de la esquina superior izquierda del mapa.
        self.downRight# (min_Y:float,max_X:float). Par de coordenadas Y-UMT, X-UMT de la esquina inferior derecha del mapa.
        self.dim# (filas:integer,columnas:integer). Dimensiones totales del grid del mapa.
        self.filename = filename
        self.f# Fichero hdf5.

    
    def umt_YX(y : float, x : float) -> float:
        """Dadas las coordenadas Y-UMT y X-UMT debe devolver el valor correspondiente a la celda del grid que corresponda a la posición de dichas coordenadas. Si no existe valor en dichas coordenadas devolverá el valor Mapa.nodata_Value."""
        ...

    
    def resize(factor : int, transform : function, nombre_nuevo : str) -> "Mapa":
        ...

