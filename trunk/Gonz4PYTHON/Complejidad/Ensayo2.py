
class Nodo:
    def __init__(self,carga):
        
        self.carga=carga
        self.siguiente=None
        
    def __str__(self):
        return str(self.carga)
        
    def obtener_carga(self):
        return self.carga
    
    def obtener_siguiente(self):
        return self.siguiente
    
    def enlazar_nodo(self,nodo):
        self.siguiente=nodo
        
class Lista_enlazada:
    def __init__(self):
        
        self.inicio=None
        self.final=None
        self.inicio2= None
        
    def agregar(self,dato):
        
        nuevo= Nodo(dato)
        
        if (self.inicio == None):# si esta vacio
            self.inicio=nuevo
            self.inicio2=self.inicio
        
        if(self.final != None):# si no esta vacio
            self.final.siguiente = nuevo # se coloca el segundo nodo
        
        self.final = nuevo
        
            
    def eliminar(self,pocicion):
        
        temp=None
        elem= self.inicio
        i=0
        
        #si la variable elem tiene un nodo  y la pocicion que le damos  es mayor q 0
        while (elem != None and i<pocicion):#el  primer elemento esta en la pocicion 0
            temp=elem
            elem= elem.siguiente
            i+=1
            
        if (temp == None):
            self.inicio= elem.siguiente
        
        else:
            #VER LA CONECCION DE COPIAS DESDE INICIO PARA VERIFICAR EL COMPORTAMIENTO DE OBJETOS MEDIANTE ESTAS COPYAS
            #OSEA COMO INFLUYE ESTE PROCEDIEMIENTO VAR TEMP Y ELEM QUE SON HIJOS DE SELF.INICIO
            temp.siguiente= elem.siguiente

    def imprimir(self):
        
        #Toma e hace una copia de todos los nodos que se adieren
        nodos = self.inicio
        
        while(nodos != None):
            print nodos.carga
            nodos= nodos.siguiente

#CREO LA LISTA ENLAZADA
l = Lista_enlazada()
l.agregar(1)
l.agregar(2)
l.agregar(3)


l.eliminar(0)
l.imprimir()




    


        