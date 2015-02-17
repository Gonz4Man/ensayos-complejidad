
class Nodo_general(object):
    def __init__(self,hijo=None,dato=None):
        
        self.__datos=dato
        self.__lista_hijos=hijo
    
    def set_dato(self,elemento):
        self.__datos.append(elemento)
    
    def set_hijo(self,hijos):
        self.__lista_hijos.append(hijos)
        
    def get_dato(self):
        return Nodo_general()
    
    def get_hijo(self):
        return self.__hijos



class Arbol_general(object):
    def __init__(self):
        self.__raiz= []#Nodo_general()
    
    def get_raiz(self):
        return self.__raiz
    
    def get_dato(self):
        pass
    def set_raiz(self,raiz):
        return self.__raiz
        
    def get_hijos(self):
        return self.__raiz.__datos
    
    def agregar_alemento(self):
        return Arbol_general.get_hijos(self)
    
    def eliminar_hijo(self,elemento):
        Arbol_general.__raiz.pop()
        
# Nodo binary de LA PLACTICA
class NodoBinarioAVL:
    def __init__(self, dato):
        self.__dato=dato
        self.__altura=0
        self.__hijo_izq = None
        self.__hijo_der = None

    def setDato(self, dato):
        self.__dato=dato
    
    def getDato(self):
        return self.__dato
    
    def setAltura(self, h):
        self.__altura=h
    
    def getAltura(self):
        return self.__altura
      
    def setHijoIzq(self, hijoIzq):
        self.__hijo_izq=hijoIzq
    
    def setHijoDer(self, hijoDer):
        self.__hijo_der=hijoDer
    
    def getHijoIzq(self):
        return self.__hijo_izq
        
    def getHijoDer(self):
        return self.__hijo_der



class ArbolAVL:
    def __init__(self, raiz=None):
        self.__raiz=raiz

    #+getRaiz():NodoBinarioAVL
    def __getRaiz(self):
        return self.__raiz
            
    #+getDatoRaiz():Object
    def getDatoRaiz(self):
        return self.__raiz.getDato()

    #+setDatoRaiz()
    def setDatoRaiz(self, datoRaiz):
        return self.__raiz.setDato(datoRaiz)
        
    def altura(self):
        if self.esVacio():
            return -1
        else:
            return self.__getRaiz().getAltura()

    def esVacio(self):
        return self.__raiz == None

    #+getHijoIzq: ArbolAVL
    def getHijoIzq(self):
        if self.__raiz == None:
            return ArbolAVL()
        else:
            return ArbolAVL(self.__raiz.getHijoIzq())
            
    def setHijoIzq(self, ab):
        self.__raiz.setHijoIzq(ab.__getRaiz())
        
    #+getHijoDer: ArbolAVL
    def getHijoDer(self):
        if self.__raiz == None:
            return ArbolAVL()
        else:
            return ArbolAVL(self.__raiz.getHijoDer())
        
    def setHijoDer(self, ab):
        self.__raiz.setHijoDer(ab.__getRaiz())
        
    def eliminarHijoDer(self):
        self.__raiz.setHijoDer(None)
        
    def eliminarHijoIzq(self):
        self.__raiz.setHijoIzq(None)

n= NodoBinarioAVL(0)
n2= NodoBinarioAVL(0)
n.setHijoDer(20)
n.setHijoIzq(12)
n2.setHijoDer(40)
n2.setHijoIzq(22)

#arbol
arbol = ArbolAVL(1)
arbol.setHijoDer(n)
arbol.setHijoIzq(n2)
print n.getDato()

