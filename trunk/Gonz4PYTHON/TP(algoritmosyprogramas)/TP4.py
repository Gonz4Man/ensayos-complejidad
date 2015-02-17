
#4 y 5)
class Temperatura(object):
    def __init__(self):
        self.tmp=0
        
    def calcular_celcius(self,grados):
        self.tmp = ((grados-32)*5)
        print "Fahrenheit a Celcius:",self.tmp/9
        
    def calcular_fahrentheit(self,fahrentheit):
        if(self.tmp >0):
            print "Calcular_celcius a Grados Fahrenheit:",(self.tmp/5)+32
        if(fahrentheit >0):
            print "Grado x a Fahrenheit:",(fahrentheit*5)

def temp():
    t1 = Temperatura()
    x= input("Ingrese G. Fahrenheit para G.Celcius:")
    t1.calcular_celcius(x)
    y= input("Convercion Grado x a Fahrenheit y su anteior:")
    t1.calcular_fahrentheit(y) 

#temp()


#6)
class Persona(object):
    def __init__(self):
        self.nombre =None
        self.apellido=None
        self.edad=None
        self.ocupacion=None
    def __str__(self):
        return ("Nombre:"+str(self.nombre)+" Apellido:"+str(self.apellido)+" Edad:"+str(self.edad)+" Ocupacion:"+str(self.ocupacion))
    def set_nombre(self,nom):
        self.nombre = nom
    def set_apellido(self,ape):
        self.apellido = ape
    def set_edad(self,anios):
        self.edad=anios
    def set_ocupacion(self,trabajo):
        self.ocupacion = trabajo
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_edad(self):
        return self.edad
    def get_ocupacion(self):
        return self.ocupacion
#7
def personal():
    p1 = Persona()
    l=[]
    
    # Hay  que tratar de buscar la manera de no instanciar me diante for
    for x in range(1,3):
        nombre= raw_input("Ingrese su nombre:")
        p1.set_nombre(nombre)
        apellido=raw_input("Ingrese su apellido")
        p1.set_apellido(apellido)
        edad = input("Ingrese su edad")
        p1.set_edad(edad)
        trabajo=raw_input("Ingrese su ocupacion:")
        p1.set_ocupacion(trabajo)
        l.append([p1])
    for x in l:
        print x 
#personal()

#8)
class Fecha(object):
    def __init__(self,dia=None,mes=None,anio=None):
        self.dia = dia
        self.mes= mes
        self.anio= anio
        
        print "Hoy es ",self.dia ,"de ",self.mes," del",self.anio
