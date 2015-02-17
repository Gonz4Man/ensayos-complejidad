import csv

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
def Socio():
    print "1)Agregar_Cliente"
    print "2)Eliminar_Cliente"
    print "3)Lista_Clientes"
    print "4)Volver"
    #archivo = open("Cliente.csv","w")#se crea automaticamente en modo escritura 
    lista_Cliente,pila =[],Pila()
    
    
    opcion= raw_input("Ingrese su Opcion :")
    if opcion == "1": 
        print "\n"
        try:
            ape =raw_input("Ingrese su Apellido :")
            if ape == "":
                raise ValueError
            nom= raw_input("Ingrese su Nombre :")
            if nom == "":
                raise ValueError
            codigo=input("Ingrese su numero de Codigo:") 
            if len(str((codigo)))> 3 or len(str((codigo))) <3:#LEVANTO UNA EXCEPCION CON ESTA CONDICION
                raise ValueError 
             
            lista_Cliente.append([ape,nom,codigo])
            pila.pelicula([ape,nom,str(codigo)])
            for x in(lista_Cliente):#ESCRIBIENDO LA DATA DE LA LISTA EN LOS ARCHIVOS CVS
                archivo = open("peliculas.csv","a")#se crea automaticamente en modo escritura
                readarchivo = csv.writer(archivo)#le corresponde el modo de escritura a x archivo
                readarchivo.writerow(x)#se escriben las lines pasandole x de la lista
            
                archivo.close()#se cierra el archivo
            print "Congratulation!!"
        except:
            print "Ingrese lo que corresponde"      
        print "1)Volver"
        condicion = raw_input("?")
        if condicion == "1": Socio()  #DE VOLVER
                      
    elif opcion == "2":
        print "1)Ultimo en lista"
        print "3)Volver"
        opcion = raw_input("Ingrese su Opcion :")
        if opcion == "1":
            print "\n"
            try:
                archivo = open("peliculas.csv","w")#se crea automaticamente en modo escritura
                #readarchivo = csv.writer(archivo)#le corresponde el modo de escritura a x archivo
                
                readarchivo.writerow("")#se escriben las lines pasandole x de la lista
                
                archivo.close()
                opcion = raw_input("?:")
            except: 
                print "Null" "\n"
                print "1)Volver"
                opcion = raw_input("?:")
                if opcion == "1": Socio()
                
        if opcion == "3":Socio()
 
    if opcion == "3":
        print "\n"
        archivo = open("peliculas.csv","r")
        readarchivo = csv.reader(archivo)
        for lineas in readarchivo:
            print lineas
               
        print "1)Volver"
        opcion = raw_input("?:")
        if opcion == "1":
            archivo.close()  
            Socio()
     
#PARA ,MANIANA ES TRATAR DE QUE AL ESCTIBIR NUEVAS CLIENTES , Y POR OPTAR LA OPCION
# DE ELIMINAR EL ULTIMO CLIENTE, Y TRATE  DE BORRAR EL ULTIMO Y NO TODOSSSS!!!!!!           
            
Socio()
