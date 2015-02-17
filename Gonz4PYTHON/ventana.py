import pygame

import csv


class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1,)
    def update(self):
        (self.left,self.top)= pygame.mouse.get_pos()
        
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    
    def update(self,pantalla,cursor):
        
        if(cursor.colliderect(self.rect)):
            self.imagen_actual = self.imagen_seleccion

        else:self.imagen_actual=self.imagen_normal
        
        
        pantalla.blit(self.imagen_actual,self.rect)
    
def main():
    pygame.init()
    
    ventana = pygame.display.set_mode([800,600])
    pygame.display.set_caption("Dibujando")
    salir = False
    reloj= pygame.time.Clock()
    
    imagen1 = pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Fondos\Fondo_menu.png")
    imagen2 = pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Fondos\Fondo2.png")
    mouse = Cursor()
    
    #Imagenes botones de las tematicas agregados  a las instancias
    b_a= pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\Astronomia1.png")
    b_a2= pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\Astronomia2.png")
    b_g=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\geo1.png")
    b_g2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\geo2.png")
    b_h=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\histo1.png")
    b_h2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\histo2.png")
    
    #Imagenes de botones del menu principal
    b_jugar1= pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\jugar1.png")
    b_jugar2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\jugar2.png")
    b_credito1=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\credito1.png")
    b_credito2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\credito2.png")
    b_salir1=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\salir1.png")
    b_salir2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\salir2.png")
    
    #Imagenes del boton de regreso al menu
    b_return1=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\Return1.png")
    b_return2=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Botones_cuadros\Return2.png")
    
    #fondos de los botones tematicos
    f_geo=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Fondos\Fondo_geo.png")
    f_astro=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Fondos\Fondo_astro.png")
    f_histo=pygame.image.load("TP(algoritmosyprogramas)\Imagenes_preguntados\Fondos\Fondo_Histo.png")
    
    #instancias del os botones del menu principal
    b_jugar= Boton(b_jugar1,b_jugar2,293,240)
    b_creditos= Boton(b_credito1,b_credito2,270,330)
    b_salir= Boton(b_salir1,b_salir2,307,414)
    
    
    #instancias de los botones tematicos
    b_astro = Boton(b_a,b_a2,293,240)
    b_geo = Boton(b_g,b_g2,304,300)
    b_histo= Boton(b_h,b_h2,313,361)
    
    b_Return_menu=Boton(b_return1,b_return2,15,550)
    semaforo = True
    
    def menu():

        ventana.blit(imagen1,(0,0))
        b_jugar.update(ventana, mouse)
        b_creditos.update(ventana, mouse)
        b_salir.update(ventana, mouse)
        pygame.display.update()
    
    while salir != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if(mouse.colliderect(b_jugar)):
                    semaforo=False
                
                if(mouse.colliderect(b_salir)):
                    exit()
                    
                if(mouse.colliderect(b_Return_menu)):
                    main()
         
                
                
        if(semaforo != False):
            #menu principal
            ventana.blit(imagen1,(0,0))
            b_jugar.update(ventana, mouse)
            b_creditos.update(ventana, mouse)
            b_salir.update(ventana, mouse)
            
        else:
            ventana.blit(imagen2,(0,0))
            #menu de las tematicas
            if(mouse.colliderect(b_astro)):
                ventana.blit(f_astro,(0,0))
            if(mouse.colliderect(b_geo)):
                ventana.blit(f_geo,(0,0))
            if(mouse.colliderect(b_histo)):
                ventana.blit(f_histo,(0,0))
                
            
            
            b_astro.update(ventana, mouse)
            b_geo.update(ventana, mouse)
            b_histo.update(ventana, mouse)
            b_Return_menu.update(ventana, mouse)
            
            
        mouse.update()
        
        reloj.tick(20)
        pygame.display.update()
    pygame.quit()    
        
main()

def dato():
    
    r1 = [0,2,1]
    
    lista1=["Jimy Hendrix","romeo santos","federico hope","gomes bolanios"]
    lista2=["Los ramones","pink Floid","Guns and roses","Metallica"]
    lista3=["1844","1969","2011","1500"]
    lista_general=[lista1,lista2,lista3]
    
    preguntas = open("Preguntas_musica.txt")
    archivo_respuestas = open("Respuestas_musica.txt")
    salir = True
    
    cont=0
    while salir != False:
        cuestionario = preguntas.readline()
        respuestas = archivo_respuestas.readline()
        
        print cuestionario
        print "a)",lista_general[cont][0] 
        print "b)",lista_general[cont][1] 
        print "c)",lista_general[cont][2] 
        print "d)",lista_general[cont][3] 
        
        responder = raw_input("Ingrese su opcion:")
        print "La respuesta correcta es: ",respuestas
        
        if(responder+"\n" == respuestas):
            print "acertaste",respuestas
        
        elif(responder == "x"):
            salir = False
        
        else: print "no acertaste"
        cont+=1 #siguiente lista de artistas
    preguntas.close()
    archivo_respuestas.close()




def Question(answer,reply,list,number,n):  

    manager1 = csv.reader(answer[number])
    manager2= csv.reader(reply[number])
    Output = True
    cont2=0
    
    if(number > 2):
        
        return 0
    
    else:
        try:   
            for x in manager1:# lee las preguntas
                for y in manager2:#lee las respuestas
                    
                    while (Output != False):
                          
                        print x[cont2]
                            
                        #Nota: Solamnete se quiere apuntala en el archivos csv a la ultima linea para
                        #no usar 1 archivos por tematica solamente para las respuestas
                        print "a)",list[n][cont2][0] 
                        print "b)",list[n][cont2][1] 
                        print "c)",list[n][cont2][2] 
                        print "d)",list[n][cont2][3]
                        
                            
                        opcion = raw_input("Escriba su respuesta: ")
                            
                        if (opcion == y[cont2]):print "acertastes"
                            
                        elif (opcion == "x"): salir = False
                             
                        else: print "No acertastes"
                        cont2+=1
            
        except(IndexError):

            return Question(answer,reply,list,number+1,n+1)
            answer.close()
            reply.close()
    
        
def date2():
    
    #abriendo archivos
    p_musica = open("P_musica.csv")
    p_historia=open("P_Historia.csv")
    p_geografia=open("P_geografia.csv")
    
    r_musica=open("R_musica.csv")
    r_historia=open("R_Historia.csv")
    r_geografia= open("R_geografria.csv")
    
    #opciones musica
    m1=["Jimy Hendrix","romeo santos","federico hope","gomes bolanios"]
    m2=["1844","1969","2011","1500"]
    m3=["Venezolano","colombiano","Thailandes","sueco"]

    #opciones de historia
    h2=["xio pang","Tsumoto shinomura","Bruce lee","gonzaRg"]
    h1=["2010 D.C","446 A.C","1608 D.C","778 D.C"]
    h3=["Argentina","Roma","Chile","Belgica"]
    
    #opciones de geografia
    g1=["Mongolia","Nueva Zelanda","Tibet","Thailandia"]
    g2=["peru","Bolivia","argentina","chile"]
    g3=["Africa","Rusia","Belgica","Australia"]
    
    answer_major=[[m1,m2,m3],[h1,h2,h3],[g1,g2,g3]]
    
    list_registry= [p_musica,p_historia,p_geografia,"No Interrumpir"]#agregado para terminar dentro de la funcion Question
    list_reply=[r_musica,r_historia,r_geografia,"No Interrumpir"]#agregado para terminar dentro de la funcion Question
    
    Question(list_registry,list_reply, answer_major,0,0)
    
    print "\nHola Funcion original"
  
    
#date2()


    


    