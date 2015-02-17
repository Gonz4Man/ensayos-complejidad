
import pygame
import time
import csv

class Imagen(object):
    def __init__(self,imagen,nombre=None,x=0,y=0):
        self.fhoto=imagen
        self.nombre=nombre
        self.x=x
        self.y=y
        self.rect = self.fhoto.get_rect()
        self.rect.left,self.rect.top = (self.x,self.y)  

    def dibujar(self,superficie):    
        superficie.blit(self.fhoto,self.rect)
        
class Imagen2(object):

    def __init__(self,imagen,x=0,y=0):
        self.fhoto=imagen
        self.x=x
        self.y=y  

    def dibujar(self,superficie):    
        superficie.blit(self.fhoto,(self.x,self.y))
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

class Preguntados():
    def __init__(self):
        
        pygame.init()
        self.ventana = pygame.display.set_mode([800,600])
        self.titulo = pygame.display.set_caption("Preguntados")
        self.reloj = pygame.time.Clock()
        self.salir =True
        self.derecho_menu = True
        self.derecho_tematica=False
        self.derecho_credito=False
        self.mouse= Cursor()
        
        #Musica General
        pygame.mixer.music.load("Sonidos\Main.mid")
        self.s_bien = pygame.mixer.Sound("Sonidos\Good.wav")
        self.s_mal= pygame.mixer.Sound("Sonidos\Fail.wav")
        self.s_toque= pygame.mixer.Sound("Sonidos\Toque.wav")

        
        #Imagenes del boton de regreso al menu  DEL MENU PRINCIPAL Y TEMATICA E INSTANCIADOS
        self.b_return1=pygame.image.load("Imagenes_preguntados\Botones_cuadros\Return1.png")
        self.b_return2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\Return2.png")
        
        self.b_Return_menu=Boton(self.b_return1,self.b_return2,15,550)
        self.b_Return_menu2=Boton(self.b_return1,self.b_return2,15,550)
        
        
        self.imagen1 = pygame.image.load("Imagenes_preguntados\Fondo_menu.png")
        
        #Imagenes de botones del menu principal
        self.b_jugar1= pygame.image.load("Imagenes_preguntados\Botones_cuadros\jugar1.png")
        self.b_jugar2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\jugar2.png")
        self.b_credito1=pygame.image.load("Imagenes_preguntados\Botones_cuadros\credito1.png")
        self.b_credito2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\credito2.png")
        self.b_salir1=pygame.image.load("Imagenes_preguntados\Botones_cuadros\salir1.png")
        self.b_salir2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\salir2.png")
        
        
        #INSTANCIAS DE LOS BOTONES DEL MENU PRINCIPAL
        self.b_jugar= Boton(self.b_jugar1,self.b_jugar2,293,240)
        self.b_creditos= Boton(self.b_credito1,self.b_credito2,270,330)
        self.b_salir= Boton(self.b_salir1,self.b_salir2,307,414)
          
        
        #IMAGENES E INSTANCIAS DE LOS B0TONES TEMATICOS   
        self.imagen2 = pygame.image.load("Imagenes_preguntados\Fondo2.png")
        self.fondo_tematico= Imagen2(self.imagen2,0,0)
        
        #fondos de los botones tematicos
        self.f_geo=pygame.image.load("Imagenes_preguntados\Fondo_geo.png")
        self.f_astro=pygame.image.load("Imagenes_preguntados\Fondo_astro.png")
        self.f_histo=pygame.image.load("Imagenes_preguntados\Fondo_Histo.png")
            
        #Imagenes botones de las tematicas agregados  a las instancias
        self.b_a= pygame.image.load("Imagenes_preguntados\Botones_cuadros\Astronomia1.png")
        self.b_a2= pygame.image.load("Imagenes_preguntados\Botones_cuadros\Astronomia2.png")
        self.b_g=pygame.image.load("Imagenes_preguntados\Botones_cuadros\geo1.png")
        self.b_g2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\geo2.png")
        self.b_h=pygame.image.load("Imagenes_preguntados\Botones_cuadros\histo1.png")
        self.b_h2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\histo2.png")
        
        
        #instancias de los botones tematicos
        self.b_astro = Boton(self.b_a,self.b_a2,293,240)
        self.b_geo = Boton(self.b_g,self.b_g2,304,300)
        self.b_histo= Boton(self.b_h,self.b_h2,313,361)
            
        
        # CREDITOS
        self.imagen3 = pygame.image.load("Imagenes_preguntados\Fondo_credito.png")
        self.Fondo_credito= Imagen2(self.imagen3,0,0)

        Preguntados.Motor(self)
        
    def Play(self,answer,reply,list,number,n):
        
        #variables numericas del juego
        self.pulsaciones=0
        self.puntaje=0
        self.cont=0
        self.cont2=0
        
        self.manager1 = csv.reader(answer[number])
        self.manager2= csv.reader(reply[number])
        
        #Fondo
        self.fondo_juego = pygame.image.load("Imagenes_preguntados\Fondo_juego.png")
        self.final_fondo=pygame.image.load("Imagenes_preguntados\Final_Puntaje.png")
        
        #Fuentes del juego
        self.fuente= pygame.font.SysFont("Harrington",25)
        self.fuente1=pygame.font.SysFont("Harrington",17)
        self.fuente2= pygame.font.SysFont("Harrington",40)
        self.fuente3= pygame.font.SysFont("Harrington",40)
        
        #BARRA DE RESPUESTAS
        self.cuadro1= pygame.image.load("Imagenes_preguntados\Botones_cuadros\Cuadro.png")
        self.cuadro2=pygame.image.load("Imagenes_preguntados\Botones_cuadros\Cuadro2.png")
        self.cuadro3=pygame.image.load("Imagenes_preguntados\Botones_cuadros\Cuadro3.png")
        
            
        #IMAGENES DE LOS BOTONES AL LADO DE LA BARRA
        self.a= pygame.image.load("Imagenes_preguntados\Botones_cuadros\B_A.png")
        self.b=pygame.image.load("Imagenes_preguntados\Botones_cuadros\B_B.png")
        self.c=pygame.image.load("Imagenes_preguntados\Botones_cuadros\B_C.png")
        self.d=pygame.image.load("Imagenes_preguntados\Botones_cuadros\B_D.png")
            
        #fuentes de los carteles en cuadros
        self.cadena_tiempo= self.fuente.render("Tiempo",False,(0,0,0))
        self.cadena_aciertos= self.fuente.render("Aciertos",False,(0,0,0))
        self.cadena_puntaje= self.fuente.render("Puntos",False,(0,0,0))
        self.loser=self.fuente2.render("Defeat",False,(255,255,255),(0,0,0))
        self.win=self.fuente2.render("Winner",False,(255,255,255),(0,0,0))
        
        #INSTANCIAS de las barras
        self.c_a= Imagen(self.cuadro1,"c_a",185,310)
        self.c_b=Imagen(self.cuadro1,"c_b",455,310)
        self.c_c=Imagen(self.cuadro1,"c_c",185,400)
        self.c_d=Imagen(self.cuadro1,"c_d",455,400)
        
        mouse= Cursor()        
        self.limpiar=self.ventana.copy()
  
        try:
            for x in self.manager1:# lee las preguntas
                for y in self.manager2:#lee las respuestas
                    while(True):
                        self.ventana.blit(self.limpiar,(0,0))
                        self.ventana.blit(self.fondo_juego,(0,0))
                            
                        self.temp=[]
                        self.lista_cuadros =[self.c_a,self.c_b,self.c_c,self.c_d]
                            
                        self.cont+=1
                               
                        #Cuadros rectangulares
                        pygame.draw.rect(self.ventana,(0,200,0),(718,20,90,80),0)
                        pygame.draw.rect(self.ventana,(0,200,0),(718,110,90,60),0)
                        
                        pygame.draw.rect(self.ventana,(255,255,255),(721,22,77,76),0)
                        pygame.draw.rect(self.ventana,(255,255,255),(721,112,77,56),0)
                            
                        #Fuente puestas en marcha de imprecion sobre los cuadros
                        self.tiempo= self.fuente2.render(str(self.cont/17),True,(0,0,0),(255,255,255))     
                        self.puntos=self.fuente.render(str(self.puntaje),False,(0,0,0))
                        self.puntaje_final=self.fuente2.render(str(self.puntaje),True,(255,255,255),(0,0,0))
                            
                        #cadenas numericas impresas en los cuadros
                        self.ventana.blit(self.tiempo,(745,50))
                        self.ventana.blit(self.puntos,(750,140))
                            
                        #cadenas impresas en los cuadros      
                        self.ventana.blit(self.cadena_tiempo,(720,25))
                        self.ventana.blit(self.cadena_puntaje,(720,113))
                            
                        self.c_a.dibujar(self.ventana)
                        self.c_b.dibujar(self.ventana)
                        self.c_c.dibujar(self.ventana)
                        self.c_d.dibujar(self.ventana)
                
                        self.ventana.blit(self.a,(150,300))
                        self.ventana.blit(self.b,(420,300))
                        self.ventana.blit(self.c,(150,390))
                        self.ventana.blit(self.d,(420,390))
                            
                        #Fuentes  e Imprecion e la pregunta
                        pregunta = self.fuente3.render(str(x[self.cont2]),False,(0,255,0))
                        self.ventana.blit(pregunta,(8,80))
                            
                        #FUENtes e imprecion de las opciones
                        p_a=self.fuente1.render(str(list[n][self.cont2][0]),True,(0,0,0))
                        p_b=self.fuente1.render(str(list[n][self.cont2][1]),True,(0,0,0))
                        p_c=self.fuente1.render(str(list[n][self.cont2][2]),True,(0,0,0))
                        p_d=self.fuente1.render(str(list[n][self.cont2][3]),True,(0,0,0))
                            
                        self.ventana.blit(p_a,(223,310))
                        self.ventana.blit(p_b,(493,310))
                        self.ventana.blit(p_c,(225,400))
                        self.ventana.blit(p_d,(493,400))
                        mouse.update()
                        
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit()
                                
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if((self.pulsaciones%2)==0):
                                         
                                    if(self.c_a.nombre == y[self.cont2] and mouse.colliderect(self.c_a)):
                                        self.c_a.fhoto= self.cuadro2
                                        self.puntaje+=10
                                        self.s_bien.play()
                                        self.lista_cuadros.remove(self.c_a)
                                                                       
                                    elif(self.c_b.nombre == y[self.cont2]and mouse.colliderect(self.c_b)):
                                        self.c_b.fhoto= self.cuadro2
                                        self.puntaje+=10
                                        self.s_bien.play()
                                        self.lista_cuadros.remove(self.c_b)
                                            
                                    elif(self.c_c.nombre == y[self.cont2]and mouse.colliderect(self.c_c)):
                                        self.c_c.fhoto= self.cuadro2
                                        self.puntaje+=10
                                        self.s_bien.play()
                                        self.lista_cuadros.remove(self.c_c)
                                                 
                                    elif(self.c_d.nombre == y[self.cont2]and mouse.colliderect(self.c_d)):
                                        self.c_d.fhoto= self.cuadro2
                                        self.puntaje+=10
                                        self.s_bien.play()
                                        self.lista_cuadros.remove(self.c_d)
                                        
                                    else:
                                        for z in range(0,len(self.lista_cuadros)):
                                            if(self.lista_cuadros[z].nombre == y[self.cont2]): 
                                                self.temp.append(self.lista_cuadros[z])
                                            self.lista_cuadros[z].fhoto=self.cuadro3    
                                        self.temp[0].fhoto= self.cuadro2
                                        self.s_mal.play()            
                                self.pulsaciones+=1
          
                            if event.type == pygame.MOUSEBUTTONUP:                
                                #Si se cliquea dos veces se cambia de pregunta y cuadros
                                if((self.pulsaciones%2)==0):
                                    
                                    for z in self.lista_cuadros: 
                                        z.fhoto= self.cuadro1
                                    self.cont2+=1    
                        
                        if(self.pulsaciones >=20):
                            if(self.puntaje >=100):
                                self.ventana.blit(self.final_fondo,(0,0))
                                self.ventana.blit(self.win,(340,330))
                                self.ventana.blit(self.puntaje_final,(381,370))
                            else:
                                self.ventana.blit(self.final_fondo,(0,0))
                                self.ventana.blit(self.loser,(340,330))
                                self.ventana.blit(self.puntaje_final,(381,370))   
                        self.reloj.tick(20)
                        pygame.display.update()
                    pygame.quit()  
                    
                                               
        except(IndexError):#Antes de regresar a las tematicas muestra puntaje y cierra archivo
            
            time.sleep(3)
            return 
            answer.close()
            reply.close()
     
    def juego(self,pos1,pos2):

        #abriendo archivos
        self.p_astronomia = open("P_Astronomia.csv")
        self.p_geografia=open("P_geografia.csv")
        self.p_historia=open("P_Historia.csv")
        
        
        #abriendo respuestas
        self.r_astronomia=open("R_Astronomia.csv")
        self.r_geografia= open("R_geografria.csv")
        self.r_historia=open("R_Historia.csv")
    
        #opciones de astronomia
        self.m1=["Priamo","Sol","Pinta","Santa Maria"]
        self.m2=["Triton","Kerberos","Andromeda","Luna"]
        self.m3=["Ulices","Halley","Antrogenia","H23G"]
        self.m4=["Via Lactea","Ganimides","Apolo","Andromeda"]
        self.m5=["   3","   6","   10","    7"]
        self.m6=["Galaxia","Estrella","Cometa","Agujero Negro"]
        self.m7=["Big Bang","Colicion Planetaria","Impacto espacial","Bomba Nuclear"]
        self.m8=["Luna","Tierra","Saturno","Jupiter"]
        self.m9=["Mercurio","H23G","Marte","Arquimides"]
        self.m10=["Gonz4 rg","Astrolavio","Alienigena","Mutante"]
        
        #opciones de geografia
        self.g1=["Mongolia","Nueva Zelanda","Tibet","Thailandia"]
        self.g2=["peru","Bolivia","argentina","chile"]
        self.g3=["Africa","Rusia","Belgica","Australia"]
        self.g4=["Buenos Aires","Ottawa","Lima","La plata"]
        self.g5=["chile","Rusia","Brazil","Canada"]
        self.g6=["Uruguay","New York","Roma","Chacarita"]
        self.g7=["Inglaterra","Thailandia","Argentina","EE.UU"]
        self.g8=["Holanda","Rusia","Belgica","Escocia"]
        self.g9=["New jersey","Rio Gallegos","Finlandia","Santa Cruz"]
        self.g10=["Africa","Oceania","America","Europa"]
        
        #opciones de historia
        self.h1=[" 2010 D.C"," 444 A.C"," 1608 D.C"," 778 D.C"]
        self.h2=["Leonardo Davinchi","Miguel Angel","Isacc Newton","Napoleon"]
        self.h3=["Argentina","Roma","Chile","Belgica"]
        self.h4=["Steve Jobs","Fhill Collin","Antonio Stradivari","Ash Kernel"]
        self.h5=["El Destripador","Harold Shipman","Ricardo iorio","Henry Bogard"]
        self.h6=["Steban kito","James Stolder","Tenenbaum","James Smithson"]
        self.h7=[" 1.7 mil A.C"," 500 D.C"," 2011 D.C"," 1.5 mil A.C"]
        self.h8=["Steve Wozniak","Steve Jobs","Bill Gates","Kevin mitnik"]
        self.h9=[" Musulmana"," Judia"," Catolica"," Profetica"]
        self.h10=["Musico Italiano"," Mercenario","10 de Boca"," Hacker"]
        
        self.answer_major=[[self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8,self.m9,self.m10],[self.g1,self.g2,self.g3,self.g4,self.g5,self.g6,self.g7,self.g8,self.g9,self.g10],[self.h1,self.h2,self.h3,self.h4,self.h5,self.h6,self.h7,self.h8,self.h9,self.h10]]
        
        self.list_registry= [self.p_astronomia,self.p_geografia,self.p_historia,"No Interrumpir"]#+1 = no Fail in range
        self.list_reply=[self.r_astronomia,self.r_geografia,self.r_historia,"No Interrumpir"]#+1 = no Fail in range
      
        self.Play(self.list_registry,self.list_reply,self.answer_major,pos1,pos2)
    
    def menu(self):
    
    
        #INSTANCIAS PUESTAS EN PANTALLA
        self.ventana.blit(self.imagen1,(0,0))
        self.b_jugar.update(self.ventana, self.mouse)
        self.b_creditos.update(self.ventana, self.mouse)
        self.b_salir.update(self.ventana, self.mouse)
        
        pygame.display.update()

   
    def tematicas(self):
    
        self.fondo_tematico.dibujar(self.ventana)
                
        #Cindicion sobre el cambio de imagen
        if(self.mouse.colliderect(self.b_astro)):
            self.ventana.blit(self.f_astro,(0,0))
        if(self.mouse.colliderect(self.b_geo)):
            self.ventana.blit(self.f_geo,(0,0))
        if(self.mouse.colliderect(self.b_histo)):
            self.ventana.blit(self.f_histo,(0,0))
        
        self.b_astro.update(self.ventana, self.mouse)
        self.b_geo.update(self.ventana, self.mouse)
        self.b_histo.update(self.ventana, self.mouse)
        
        self.b_Return_menu.update(self.ventana,self.mouse)

    def credito(self):
    
        self.Fondo_credito.dibujar(self.ventana)
        self.b_Return_menu2.update(self.ventana, self.mouse)  

  
    def Motor(self):
    
        self.derecho_menu= True
        self.derecho_credito=False
        self.derecho_tematica=False
        self.clear= self.ventana.copy()
        pygame.mixer.music.play(3)
        while(True):
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
                elif(event.type == pygame.MOUSEBUTTONUP):
                    
                    if(self.mouse.colliderect(self.b_jugar)):
                        self.s_toque.play()
                        self.derecho_menu = False
                        self.derecho_tematica=True                   
                
                    elif(self.mouse.colliderect(self.b_creditos)):
                        self.s_toque.play()
                        self.derecho_menu = False
                        self.derecho_tematica=False
                        self.derecho_credito= True
                        
                    elif(self.mouse.colliderect(self.b_salir)):
                        self.s_toque.play()
                        exit()
                    
                    elif(self.mouse.colliderect(self.b_Return_menu)):
                        self.s_toque.play()
                        Preguntados.Motor(self)
                    
                    elif(self.mouse.colliderect(self.b_Return_menu2)):
                        self.s_toque.play()
                        Preguntados.Motor()
                    
                    elif(self.mouse.colliderect(self.b_astro)):
                        self.s_toque.play()
                        Preguntados.juego(self,0,0)
                        
                    elif(self.mouse.colliderect(self.b_geo)):
                        self.s_toque.play()
                        Preguntados.juego(self,1,1)
                        
                    elif(self.mouse.colliderect(self.b_histo)):
                        self.s_toque.play()
                        Preguntados.juego(self,2,2)  
            
            if(self.derecho_menu == True):
            
    
                (self.b_jugar.rect.left,self.b_jugar.rect.top)=(293,240)
                (self.b_creditos.rect.left,self.b_creditos.rect.top)=(270,330)
                (self.b_salir.rect.left,self.b_salir.rect.top)=(307,414)
                Preguntados.menu(self)
                
            elif(self.derecho_credito == True):
             
                #(b_jugar.rect.left,b_jugar.rect.top)=(0,0)
                #(b_creditos.rect.left,b_creditos.rect.top)=(0,0)
                (self.b_salir.rect.left,self.b_salir.rect.top)=(-100,0)
                
                (self.b_astro.rect.left,self.b_astro.rect.top)=(-100,0)
                (self.b_geo.rect.left,self.b_geo.rect.top)= (-100,0)
                (self.b_histo.rect.left,self.b_histo.rect.top)=(-100,0) 
                
                Preguntados.credito(self)
          
            elif(self.derecho_tematica == True):
              
                (self.b_astro.rect.left,self.b_astro.rect.top)=(293,240)
                (self.b_geo.rect.left,self.b_geo.rect.top)= (304,300)
                (self.b_histo.rect.left,self.b_histo.rect.top)=(313,361)
                
                (self.b_jugar.rect.left,self.b_jugar.rect.top)=(-100,0)
                (self.b_creditos.rect.left,self.b_creditos.rect.top)=(-100,0)
                (self.b_salir.rect.left,self.b_salir.rect.top)=(-100,0)
                
                Preguntados.tematicas(self)
                 
            self.mouse.update()
            self.reloj.tick(15)
            pygame.display.update()
        pygame.quit() 

        
juego = Preguntados()

        
    