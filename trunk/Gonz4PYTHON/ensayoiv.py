
import csv # SE IMPORTA EL MODULO  

class Pila(object):
    def __init__(self):
        self.pedido =[]
        
    def pelicula(self,pelicula):
        self.pedido.append(pelicula)
    
    def devolucion(self):
        if self.vacia():#PARA PODER USARLA EN UN IF EN LA ACCION DE SI ESTA VACIA 
            None        #USAMOS EL SELF.VACIA() ETC PARA QUE FUNCIONE LA MISMA 
        else:
            self.pedido.pop()
    
    def vacia(self):
        if len(self.pedido) == 0:
            return True
        else:
            return False
        
def Videoclub():
    print "**//VIDEOCLUB//**"
    pila= Pila()
    #archivo = open("peliculas.csv","w")#se crea automaticamente en modo escritura
    def main():
        print "1)Socio" 
        print "2)No_Socio"
        print "3)Stock_Peliculas"
        print "4)Salir"   
        opcion = raw_input("Ingrese su opcion :")
        if opcion == "1":
            Socio()
            condicion = raw_input("?")
            if condicion == "a":
                return main()
            else: 
                print "Ocurrio un error,Ingrese mas Tarde"
                exit()
        
        elif opcion == "2":
            print "\n"
            pass
            print "a)volver"
            condicion = raw_input("?")
            if condicion == "a":
                return main()
            else: 
                print "Ocurrio un error,Ingrese mas Tarde"
                exit()
        
        if opcion == "3":
            
            archivo = open("peliculas.csv","r")
            read = csv.reader(archivo)
            for x in read:
                print x
            archivo.close()
                
            print "a)volver"
            condicion = raw_input("?")
            
            if condicion == "4":
                return main()
            else: 
                print "Ocurrio un error,Ingrese mas Tarde"
                exit()
    
        elif opcion == "5":
            exit()
    main()
def Socio():
    print "1)Agregar_Cliente"
    print "2)Eliminar_Cliente"
    print "3)Lista_Clientes"
    print "4)Volver"
    #archivo = open("Cliente.csv","w")#se crea automaticamente en modo escritura 
    lista_Cliente=[]
    try:
        opcion= raw_input("Ingrese su Opcion")
        if opcion == "1":
            ape =raw_input("Ingrese su Apellido :")
            nom= raw_input("Ingrese su Nombre :")
            codigo=input("Ingrese su numero de Codigo:") 
            if len(str((codigo)))> 3 or len(str((codigo))) <3:#LEVANTO UNA EXCEPCION CON ESTA CONDICION
                raise ValueError 
                
            lista_Cliente.append([ape,nom,codigo])
      
            for x in(lista_Cliente):#ESCRIBIENDO LA DATA DE LA LISTA EN LOS ARCHIVOS CVS
                archivo = open("peliculas.csv","w")#se crea automaticamente en modo escritura
                readarchivo = csv.writer(archivo)#le corresponde el modo de escritura a x archivo
                readarchivo.writerow(str(x+"\n"))#se escriben las lines pasandole x de la lista
                archivo.close()#se cierra el archivo
            print "1)Volver"
            condicion = raw_input("?")
            if condicion == "1": 
                return Socio()           
           
      
    except:
        print "Ingrese lo que corresponda"
        print "Acuerdese que son 3 Enteros La cant. de digitos" 
        print "Verifique en escribir bien los atributos"
        print "No aportar Valores Falsos,etc"
            
        #pila.devolucion()
        
    if opcion == "4":#OLVIENDO AL MENU
        return Videoclub()  
Videoclub()
        
             