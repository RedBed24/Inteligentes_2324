class AsciiGrid:
    """Representa un mapa leido de un fichero de formato ASCII Grid"""

    def __init__(self, filename : str) -> None:
        """Crea un nuevo objeto con el nombre del fichero, pero no lo lee"""
        self.filename = filename
        self.read()


    def read(self) -> "AsciiGrid":
        """Lee el fichero y devuelve el objeto con los datos leidos"""
        with open(self.filename, "r") as file:
            self.ncol = int(file.readline().split()[1])
            self.nrow = int(file.readline().split()[1])
            self.xllcorner = float(file.readline().split()[1])
            self.yllcorner = float(file.readline().split()[1])
            self.cellsize = int(file.readline().split()[1])
            self.no_data_value = float(file.readline().split()[1])

            self.map = []

            for line in file:
                self.map.append([])
                for value in line.split():
                    # FIXME: Ponemos None en vez de no_data_value???
                    self.map[-1].append(float(value) if value != self.no_data_value else None)

        return self


    def __str__(self) -> str:
        return f"AsciiGrid({self.filename}, {self.ncol=}x{self.nrow=}, {self.xllcorner=}, {self.yllcorner=}, {self.cellsize=}, {self.no_data_value=})"

    
    def __repr__(self) -> str:
        return self.__str__()

