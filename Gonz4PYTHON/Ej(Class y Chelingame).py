
# class Punto(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     
#     def sumar(self):#metodo dentro de la clase
#         print self.x + self.y
#         
# punto = Punto(50,60)
# print punto.x
# print punto.y  
# punto.sumar()   


# class Auto(object):
#     #inicializamos con el constructor
#     def __init__(self,color="sin color",marca="sin marca",prendido=False):
#         #atributos del METODO auto
#         self.color=color 
#         self.marca=marca
#         self.estaprendido=prendido
#         
#     def __str__(self):#cambia lo que se imprime en el print si imprimo a1 solamente
#         #osea este metodo especial hace que cuando imprima la clase PUNTO
         #Me imprima esta cadena ;)!!!!!!!!!!!!!!!!!
#         if self.estaprendido:
#             estado = "Prendido"
#             
#         else:
#             estado= "Apagado"
#         
#         return " el Auto " + str(self.marca)+" de color "+ str(self.color)+ " esta " +str(estado)
#         
#     
#     
#     
#     #METODO ARANCAR
#     def arancar(self):
#         if self.estaprendido:
#             print "el auto esta prendido"
#             
#         else:
#             self.estaprendido= True
#             print "el auto aranco"
#     
#     
#                     
# a1= Auto()
# a1.arancar()
#print a1
# 
# class Punto(object):
#     #metodo constructor
#     def __init__(self,x=0,y=0):
#         
#         self.x=x
#         self.y=y
#         
#     def __str__(self):
#         #osea este metodo especial hace que cuando imprima la clase PUNTO
#         #Me imprima esta cadena ;)!!!!!!!!!!!!!!!!!
#         return "x:"+str(self.x)+ "  y:" + str(self.y)
#         
#     # metodo para sumarrrr        
#     def __add__(self,otro):
#         return Punto(self.x+otro.x,self.y+otro.y)
#     
#     #METODO DE LA RESTA
#     def __sub__(self,otro):
#         return Punto(self.x-otro.x,self.y-otro.y)
#         
#     #METODO DE SOBRE SI DOS PUNTOS SON == , OSEA METODO DE COMPARACION
#     def __cmp__(self,otro):
#         if self.x == otro.x and self.y == otro.y:
#             #si devuelve 0 es que son iguales los puntos
#             #es que este metodo esta hecho para que sea asy
#             return 0
# 
# class Pj(object):
#     def __init__(self,level=1):
#         self.level=level
# 
#     def __cmp__(self,otro):
#         #atributo
#         if self.level < otro.level:
#             return -1
#         
#         #atributo
#         elif self.level > otro.level:
#             return 1
#         
#         #atributo del =
#         else:
#             return 0
#      
# humano = Pj(3)
# ogro = Pj(3)


#clase madre de las demas que ando usando
# class Guerrero(object):
#     
#     def __init__(self,nombre="Guerrero"):
#         self.hp= 100
#         self.mp= 50
#         self.nombre = nombre
#         
#     def atacar(self):
#         print "el jugador", self.nombre,"ataco"    
#         
#             
# 
# #clase elfo hereda de guerrero
# class Elfo(Guerrero):
#     def __init__(self,nombre="Elfo"):#contructor del elfo
#         
#         #ya importamos o heredados los metodos de class Guerrero con lo sig
#         Guerrero.__init__(self, nombre)
#         
#         #atributo de la clase Elfo/SUS FLECHAS como CARACTERISTICA
#         self.flechas= 10
#     
#     
#     #METODO indiferentes de class Elfo/ACCION
#     def arco(self):
#         print "El jugador ataco con su arco"
#         self.flechas-=1
#     
# class Humano(Guerrero):
#     def __init__(self, nombre="Humano"):
#         Guerrero.__init__(self, nombre)
#     
#         #ATRIBUTO DEL HUMANO
#         self.estado_escudo=100
#     
#     #Metodo bloquiar
#     def bloquear(self):
#         print self.nombre , "Bloquio el ataque"
#         self.estado_escudo-=20
#             
# 
import random 
class Jugador(object):
    def __init__(self,nombre="Jugador"):
        self.nombre= nombre
        self.hp_max=random.randrange(45,55)
        self.mp_max=random.randrange(40,50)
        self.fuerza=random.randrange(2,7)
        self.inteligencia=random.randrange(2,5)
        #hp y mp estan igualados pero no va a variar si disminuye solo toma el valor inicial
        self.hp=self.hp_max
        self.mp=self.mp_max
        self.habilidades = [Bola_de_fuego(),Golpe_letal(),Golpiar()]
    
    def __str__(self):
        return " HP " +str(self.hp_max)+"/"+str(self.hp)
    
    def stat(self):
        print self.nombre
        print "HP: ",self.hp_max,"(Max)","/",self.hp
        print "MP: ",self.mp_max,"(Max)","/",self.mp
        print "Fuerza: ", self.fuerza
        print "Inteligencia: ",self.inteligencia
    
    def eleccion(self):
        print "Elija una habilidad"
        print "0-Bola de Fuego(**10MP)"
        print "1-Golpe Letal(**5MP)"
        print "2-Golpiar(no requiere mp)" 
        x= input("? ")   
        return x       

class Ai(object):
    def __init__(self,nombre= "PC"):
        self.nombre = nombre
        self.hp_max=random.randrange(45,55)
        self.mp_max=random.randrange(40,50)
        self.fuerza=random.randrange(2,7)
        self.inteligencia=random.randrange(2,5)
        self.hp=self.hp_max
        self.mp=self.mp_max
        self.habilidades=[Bola_de_fuego(),Golpe_letal(),Golpiar()]
    def __str__(self):
        return str(self.nombre) + "  HP: " + str(self.hp_max)+"/"+str(self.hp)    
    def stat(self):
        print self.nombre
        print "HP: ",self.hp_max,"(Max)","/",self.hp
        print "MP: ",self.mp_max,"(Max)","/",self.mp
        print "Fuerza: ", self.fuerza
        print "Inteligencia: ",self.inteligencia    
    def eleccion(self):
        x=random.randrange(0,3)
        return x

class Bola_de_fuego(object):
    def __init__(self):
        self.nombre= "Bola de Fuego"
        self.dano=0
    def devolver_ataque(self,origen):
        if origen.mp < 10:
            return 0
        else:  
            self.dano=random.randrange(13,19)+origen.inteligencia
            origen.mp+= -10
            return self.dano
    
        
class Golpe_letal(object):
    def __init__(self):
        self.nombre= "Golpe Letal"
        self.dano = 0
    def devolver_ataque(self,origen):
        if origen.mp < 5:
            return 0
        else:
            self.dano = random.randrange(7,15)+origen.fuerza
            origen.mp-=5
            return self.dano
        
class Golpiar(object):
    def __init__(self):
        self.nombre = "Golpiar"
        self.dano= 0
    def devolver_ataque(self,origen):
        self.dano= origen.fuerza+ origen.inteligencia
        return self.dano
    
                  
def main():
    print "Bienvenido a GONZ4GAME"
    print ""
    
    name = raw_input("Ingrese su nombre :")
    j1 = Jugador(name)
    j2 = Ai()
    
    #llamo e imprimo a los stats
    print "Stats del Jugador1"
    j1.stat()
    x= raw_input("...")
    print "Stats del jugador2"
    j2.stat()
    x= raw_input("...")
    while j1.hp > 0 and j2.hp >0:
        print "Turno J1"
        print j1
        print "MP" , j1.mp
        
        print j2
        elec1 = j1.eleccion()
        print "Se utilizo la Habilidad",j1.habilidades[elec1].nombre
        dano1 = j1.habilidades[elec1].devolver_ataque(j1)
        print "Danio efectuado", dano1
        j2.hp-=dano1
        
        
        if j1.hp <=0 and j2.hp <=0:
            break
        
        
        print "...."
        print "Turno J2"
        print j1
        print j2
        x= raw_input("...")
        print "MP", j1.mp
        elec2 = j2.eleccion()
        print "Se utilizo la Habilidad",j2.habilidades[elec2].nombre
        dano2=j2.habilidades[elec2].devolver_ataque(j2)
        print "dano efectuado",dano2
        j1.hp-=dano2
        x= raw_input("....")
    if j1.hp >0:
        print "Gano J1"
    else:
        print "Gano J2"        
main()
        
    
       
