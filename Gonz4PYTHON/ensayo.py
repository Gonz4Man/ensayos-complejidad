
class listasconListas(object):
    def __init__(self):
        self.__datos=[]
        
    def elemento(self,pos):
        return self.__datos[pos]
    
    def agregar(self,pos,elem):
        self.__datos[pos].append(elem)
    
    def eliminar(self,pos):
        self.__datos.pop([pos])

    def esVacia(self):
        if(self.__datos == None):return True
        
    def incluye(self,elem):
        return elem in self.__datos
    
    def set_datos(self,elem):
        self.datos.append(elem)
    
    def get_datos(self):
        return self.datos   
            
class Nodo(object):
    def __init__(self,dato=None,siguiente=None):
        self.__dato=dato
        self.__siguiente=siguiente
    
    def set_dato(self,elem):
        self.__dato=elem
    
    def set_siguiente(self,sig):
        self.__siguiente=sig
    
    def get_dato(self):
        return self.__dato
    
    def get_siguiente(self):
        return self.__siguiente
    def __str__(self):
        return str(self.__dato)   
         
class Lista_enlazada(Nodo):
    def __init__(self):
        
        self.__inicio = None
    
    def elemento(self,l,pos):
        return l[pos]
    
    def agregar(self,elem,pos):
        
        
        if(pos == 0):
            self.temp= Nodo(elem)
            #creo el nuevo nodo
            self.temp.set_siguiente(self.__inicio) #coloco en siguiente del nodo creado  el primero
            self.__inicio = self.temp # en la pocicion 0 coloco el nuevo nodo
        else:
            self.temp2= Nodo(elem)
            self.__inicio
            
             
    def eliminar(self,pos):
        if (pos == None):
            pos = self.len - 1
        if(pos == 0):
            self.dato = self.__inicio
            self.prim = self.__inicio.get_siguiente()
            
    def esVacia(self):
        if (len(self.__inicio) >=0): return False
        else: True
    
    def incluye(self,elem):
        return elem in self.__inicio
    
    def __str__(self):
        
        return str(self.__inicio)

l1= Lista_enlazada()
l1.agregar("nod1",0)
print l1



class Lista(Lista_enlazada,listasconListas):
    def __init__(self):
        
        self.tamanio = 0
 
    
    def recorredor(self):
        return Recorredor()
   
    def get_tamanio(self):
        return self.tamanio
    
    def __str__(self):
        return str(self.__datos)
l=Lista_enlazada()
l.agregar(0, "n1")
print l





   
class Recorredor(Lista):
    def __init__(self,):
        
        Lista.__init__(self)
        
        self.__lista=Lista.__inicio
        self.__actual=0
        
        if(self.lista == None):
            print "No se agregaron elementos"
        else:self.actual= [self.lista[self.actual]]
         
        
    def Comenzar(self):
        for x in range(0,len(self.__lista)):
            print self.__lista[x]
    
    def elemento(self):
        Lista.elemento(self, self.__actual)
    
    def proximo(self):
        self.actual+=1 
        
    def fin(self):
        
        if( self.lista[-1] == self.lista[self.actual]):
            print "Llego al Final: ",self.lista[self.actual]
        
        else: print " No se llego al final"
        
    def agregar(self,elem):
        
        #el elemento der la pocicion actual es reemplazado por el nuevo
        #y el valor viejo es mandado al final de la lista principal
        self.temp=self.lista[self.actual]
        self.lista[self.pocicion]=elem
        self.lista.append(self.temp)    
        
    def eliminar(self):
        del self.lista[self.actual]

  


