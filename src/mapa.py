# TODO: Implementar la clase Mapa
class Mapa:
    def __init__(self, filename : str) -> None:
        self.filename = filename
        self.f, self.nodata_Value, self.sizeCell, self.upLeft, self.downRight, self.dim = leer hdf5(self.filename)# Fichero hdf5.
        # nodata_Value float. Valor para las celdas del grid que no contienen un valor válido. Si el mapa tiene más de un dataset este valor debe ser igual para todos.
        # sizeCell float. Tamaño en metros de un lado de la celda de un dataset. Si existen varios datasets este valor debe ser similar en todos.
        # upLeft (max_Y:float,min_X:float). Par de coordenadas Y-UMT, X-UMT de la esquina superior izquierda del mapa.
        # downRight (min_Y:float,max_X:float). Par de coordenadas Y-UMT, X-UMT de la esquina inferior derecha del mapa.
        # dim (filas:integer,columnas:integer). Dimensiones totales del grid del mapa.


        self.nombres_ordenados = []

    
    def umt_YX(self, y : float, x : float) -> float:
        """Dadas las coordenadas Y-UMT y X-UMT debe devolver el valor correspondiente a la celda del grid que corresponda a la posición de dichas coordenadas. Si no existe valor en dichas coordenadas devolverá el valor Mapa.nodata_Value."""
        for fichero in self.nombres_ordenados:
            leer datos del dataset
            leer xinf, yinf, xsup, ysup, cellsize, nodata_value # atributos del dataset, se leen en hdf5_data_handler
            if yinf < y and y < ysup and xinf < x and x < xsup:
                return mapa[int((y - yinf)/cellsize)][int((x - xinf)/cellsize)]
        
        return self.nodata_value

    
    def resize(self, factor : int, transform : function, nombre_nuevo : str) -> "Mapa":

            crear hfd5(todos los datos nuveos):
                clonar(self.f a f_n = File(nombre_nuevo))
                editar(f_n, factor, transform):
                    for dataset in f_n: # dataset es el nombre del dataset
                        leer data_antiguo #data_antiguo=leer(dataset.data)
                        leer xinf, yinf, xsup, ysup, cellsize, nodata_value

                        # editar atributos de cada dataset y escribirlos en el hdf5
                        dataset.cellsize = cellsize * factor
                        
                        # editar data del cada daataset y escribitlo en el hdf5 (borrar, crear nuevo data y escribir)
                        borrar(f_n, dataset)
                        data_nuevo=np.numpy()
                        for i in range (0, len(data_antiguo), factor):
                            data_nuevo.append(np.numpy())
                            for j in range (0, len(data_antiguo[0]), factor):
                                value = transform(data_antiguio[i:i+factor-1][j:j+factor-1])
                                data_nuevo[-1].append(value)
                        escribir(f_n, dataset, data_nuevo)




        
            return Mapa(nombre_nuevo) # ya se encarga de leer las dims, constructor mapa más exactamente leer hdf5
                
                    

            

