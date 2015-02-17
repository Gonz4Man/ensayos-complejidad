
class Nodo_general(object):
    def __init__(self):
        self.__datos=[]
        self.__lista_hijos=[]
        
    def get_dato(self):
        pass
    
    def set_dato(self):
        pass
    
    def get_hijos(self):
        return self.__lista_hijos
    
    def set_hijos(self,elem):
        self.__lista_hijos.append(elem)
        
class dato:
    def __init__(self,datos):
        self.__dato= datos
        
    def set_datos(self,elem):
        self.__dato(elem)
    
    def get_dato(self):
        return self.__dato
    
class prueba:
    def __init__(self,data=None):
        self.__carga= data
        
    def get_carga(self):
        return self.__carga.get_dato()
    
i1= dato(2)
p1= prueba(i1)
print i1.get_dato()
print p1.get_carga()
        