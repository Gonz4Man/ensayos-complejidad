
class Lista(object):
    def __init__(self):
        self.datos=[]
        self.cantidad_datos= 0
    
    def agregar(self,valor):
        self.datos.append(valor)
        self.cantidad_datos+=1
    
    def borrar(self,valor):
        del self.datos[valor]
        self.cantidad_datos-=1
    
    def ver(self):
        for x in self.datos:
            print x
        
class Lista_simple(Lista):
    def __init__(self):
        self.pocicion_actual=0
    
    def siguiente(self):
        return self.datos[self.pocicion_actual]
        self.pocicion_actual+=1
    
    def comienzo(self):
        self.pocicion_actual=0
        
l= Lista()
l.agregar("Hola")
l.agregar("gonzalo")
l.agregar("como")
l.agregar("estas")

print "muestra los datos ingresados"
l.ver()
print l.cantidad_datos
print "\nBorro el primer elemento"
l.borrar(0)
l.ver()
print "veo la ogitud de los elementos"
print l.cantidad_datos
        
l2 = Lista_simple()
l2.siguiente()
print l2.pocicion_actual      
        
        