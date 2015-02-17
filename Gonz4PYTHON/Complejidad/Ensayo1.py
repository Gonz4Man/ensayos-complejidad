class Arbol :

    def __init__(self, carga, izquierda=None, derecha=None):
        
        self.carga = carga
        
        self.izquierda = izquierda
        self.derecha = derecha

    def __str__(self) :
        return str(self.carga)

    def return_Carga(self):
        return self.carga

    def return_Izquierda(self):
        return self.izquierda

    def return_Derecha(self):
        return self.derecha

    def ingresa_Carga(self, carga):
        self.carga = carga

    def ingresa_Izquierda (self, izquierda):
        self.left = izquierda

    def ingresa_Derecha(self, derecha):
        self.derecha = derecha
    
def total(arbol):
    if (arbol == None) :
        return 0

    return total(arbol.izquierda) + total(arbol.derecha) + arbol.carga

def imprimeArbol(arbol):
    if arbol == None:
        return

    print arbol.carga,
    imprimeArbol(arbol.izquierda)
    imprimeArbol(arbol.derecha)
    
def imprimeArbolPosfijo(arbol):
    if arbol == None:
        return

    imprimeArbolPosfijo(arbol.izquierda)
    imprimeArbolPosfijo(arbol.derecha)
    print arbol.carga

def imprimeArbolInfijo(arbol):
    if arbol == None:
        return

    imprimeArbolInfijo(arbol.izquierda)
    imprimeArbolInfijo(arbol.derecha) 
    print arbol.carga
    
def imprimeArbolSangrado(arbol, nivel=0):
    if arbol == None:
        return

    imprimeArbolSangrado(arbol.derecha, nivel+1)
    imprimeArbolSangrado(arbol.izquierda, nivel+1)
    print ' '*nivel + str(arbol.carga)

a= Arbol("item1")
b= Arbol("item2")

      