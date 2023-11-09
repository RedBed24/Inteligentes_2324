from estado import Estado
from accion import Accion  
from nodo import Nodo
from typing import Optional

class Nodo:

    last_id=0

    def __init__(self, estado:Estado, valor:float, profundidad:int, costo:float, heuristica:float, accion:Accion,parent: Optional['Nodo'] = None):
        self.id=Nodo.last_id
        Nodo.last_id+=1
        self.parent=parent
        self.estado=estado
        self.valor=valor
        self.profundidad=profundidad
        self.coste=costo
        self.heuristica=heuristica
        self.accion=accion

    def __str__(self):
        return f"[{self.id}][{self.coste},{self.estado.id},{self.parent.id},{self.accion},{self.profundidad},{self.heuristica},{self.valor}]"
    
    def __repr__(self):
        return self.__str__()   
    
    def funcion_camino(self):
        camino=[self]

        if self.parent is not None:
            camino+=self.parent.funcion_camino()
        
        return 
    
    def __eq__(self, other) -> bool:
        return self.id==other.id
    
    def __lt__(self, other) -> bool:
        return self.id<other.id
    
    def __le__(self, other) -> bool:
        return self.id <= other.id 


    def __gt__(self, other) -> bool:
        return self.id > other.id

    def __ge__(self, other) -> bool:
        return self.id >= other.id



