from estado import Estado
from mapa import Mapa

class Problema:
    def __init__(self, filename : str, y_0 : float, x_0 : float, y_d : float, x_d : float) -> None:
        self.map = Mapa(filename)
        self.initial_state = Estado(y_0, x_0, self.map)
        self.end_state = Estado(y_d, x_d, self.map)
    
    def objetivo(self, state : Estado) -> bool:
        return state == self.end_state
