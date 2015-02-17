import pygame
import os , sys
import random

    
pygame.init()
 
ventana = pygame.display.set_mode([900,720])
pygame.display.set_caption("ventana")

#FUENTES DE LAS PALABRAS
fuente= pygame.font.SysFont("Comic Sans MS",50)#palabras de animales
fuente1= pygame.font.SysFont("Comic Sans MS",60)
fuente2= pygame.font.SysFont("Harrington",25)
fuente3= pygame.font.SysFont("Harrington",35)
fuente4= pygame.font.SysFont("Harrington",45)

reloj = pygame.time.Clock()

#PORTADA DE AYUDA Y DEL MENU
menu = pygame.image.load("juego/Palabras Locas.jpg")
help= pygame.image.load("juego/ayuda.jpg")
musicamenu= pygame.mixer.music.load("juego/Menu.mid")


def main():
      
        ventana.blit(menu,(-25,0))
       
def ayuda():
    while True:
         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    exit()
                if event.key == pygame.K_m:
                    principal()   
        ventana.blit(help,(-25,0))    
        pygame.display.update()
def juego2():
    # agrego un spacio porq sino me da error,tema de la siguiente palabra
    animales = ["pez","pantera","morza","camello","murcielago","lobo","iguana","mantaraya","codornis","loro",""]
    ganaste = fuente1.render("GANASTE",True,(255,0,0),(0,0,0))
    perdiste = fuente1.render("PERDISTE",True,(255,0,0),(0,0,0))
    ordenpala=0
    ani1 = fuente.render(animales[ordenpala],True,(0,0,0),(255,255,255))
    reloj = pygame.time.Clock()
    fondo = pygame.image.load("juego/selva final1.JPG")
    
    #musica
    juego= pygame.mixer.music.load("juego/mickey.mid")
    
    #sonidos
    s1= pygame.mixer.Sound("juego/ding.wav")#acierto en palabras
    s2= pygame.mixer.Sound("juego/chord.wav")#mal tipeado en palabras
    
    limpiar = ventana.copy()
    aciertos= 0
    total = 0
    total2 =0
    #resul = total - total2
    cadena = ""
    y,x = 0,30 
    cont=0
    

    pygame.mixer.music.play()
    
    
    def carita1():
        
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))
        pygame.draw.rect(ventana,(0,200,0),(30,30,840,662),0)#RECTANGULO FONDO
        
        #CARITA
        pygame.draw.circle(ventana,(250,250,20),(435,200),100,0)#cabeza
        pygame.draw.circle(ventana,(255,255,255),(395,170),20,0)#ojo izquierdo
        pygame.draw.circle(ventana,(255,255,255),(480,170),20,0)#ojo derecho
        pygame.draw.circle(ventana,(0,0,0),(395,175),7,0)#yema izquierda
        pygame.draw.circle(ventana,(0,0,0),(480,175),7,0)#yema derecha
        pygame.draw.line(ventana,(0,0,0),(380,230),(400,260),5)
        pygame.draw.line(ventana,(0,0,0),(400,260),(440,265),5)
        pygame.draw.line(ventana,(0,0,0),(440,265),(470,257),5)
        pygame.draw.line(ventana,(0,0,0),(470,257),(488,231),5)
        pygame.draw.circle(ventana,(250,0,0),(435,200),10,0)#NARIZ
        
        #recuadre del MENU
        pygame.draw.rect(ventana,(0,0,0),(29,645,140,47),2)
        
        #OPCION DE RETORNAR A MENU  
        retorno= fuente3.render(" (M)Menu",True,(255,0,0),(0,200,0))
        ventana.blit(retorno,(30,648))
        
        #SIN OPCION DE SIGUIENTE NIVEL
        
        
        
        reloj.tick(10)
        pygame.display.update()
    
    def carita2():
        
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))
        #RECTANGULO FONDO
        pygame.draw.rect(ventana,(0,200,0),(30,30,840,662),0)
        
        #CARITA
        
        pygame.draw.circle(ventana,(250,250,20),(435,200),100,0)#cabeza
        pygame.draw.circle(ventana,(255,255,255),(395,170),20,0)#ojo izquierdo
        pygame.draw.circle(ventana,(255,255,255),(480,170),20,0)#ojo derecho
        pygame.draw.circle(ventana,(0,0,0),(395,175),7,0)#yema izquierda
        pygame.draw.circle(ventana,(0,0,0),(480,175),7,0)#yema derecha
        pygame.draw.line(ventana,(0,0,0),(390,260),(420,250),5)
        pygame.draw.line(ventana,(0,0,0),(420,250),(455,250),5)
        pygame.draw.line(ventana,(0,0,0),(455,250),(482,260),5)
        pygame.draw.circle(ventana,(250,0,0),(435,200),10,0)#NARIZ 
       
        #recuadre del MENU
        pygame.draw.rect(ventana,(0,0,0),(29,645,140,47),2)
        
        #OPCION DE RETORNAR A MENU  
        retorno= fuente3.render(" (M)Menu",True,(255,0,0),(0,200,0))
        ventana.blit(retorno,(30,648))  
        
        
        reloj.tick(5)
        pygame.display.update()          
   
        
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))
        #RECTANGULO FONDO
        pygame.draw.rect(ventana,(0,200,0),(30,30,840,662),0)
        
        #CARITA
        
        pygame.draw.circle(ventana,(250,250,20),(435,200),100,0)#cabeza
        pygame.draw.circle(ventana,(255,255,255),(395,170),20,0)#ojo izquierdo
        pygame.draw.circle(ventana,(255,255,255),(480,170),20,0)#ojo derecho
        pygame.draw.circle(ventana,(0,0,0),(395,175),7,0)#yema izquierda
        pygame.draw.circle(ventana,(0,0,0),(480,175),7,0)#yema derecha
        pygame.draw.line(ventana,(0,0,0),(390,260),(420,250),5)
        pygame.draw.line(ventana,(0,0,0),(420,250),(455,250),5)
        pygame.draw.line(ventana,(0,0,0),(455,250),(482,260),5)
        pygame.draw.circle(ventana,(250,0,0),(435,200),10,0)#NARIZ 
        
        #OPCION DE RETORNAR A MENU  
        retorno= fuente3.render(" (M)Menu",True,(255,0,0),(0,0,0))
        ventana.blit(retorno,(30,647))  
        
        
        reloj.tick(5)
        pygame.display.update()          
      
    while True:
        y +=10
        cont+=1
        resul = total + total2
        r= random.randrange(0,255)
        g= random.randrange(0,255)
        b= random.randrange(0,255)
        
        ventana.blit(limpiar,(0,0))
        ventana.blit(fondo,(0,0))
        
        #CAIDA DE LAS PALABRAS DE ANIMALESSSS
        ani1 = fuente.render(animales[ordenpala],0,(0,230,0))
        ventana.blit(ani1,(x,y))    
        
        #FUENTES DE LAS LETRAS TIPEADAS EN PANTALLA
        letras = fuente4.render(cadena,0,(0,255,0))
        ventana.blit(letras,(10,650)) 
        
        #CUADRO DE PUNTAJES VIDAS ETC
        pygame.draw.rect(ventana,(255,255,255),(810,20,90,80),0)
        pygame.draw.rect(ventana,(255,255,255),(810,120,90,60),0)
        pygame.draw.rect(ventana,(255,255,255),(810,200,90,60),0)
                
        t1= fuente2.render("Tiempo",True,(0,0,0),(255,255,255))
        ventana.blit(t1,(820,23)) 
        
        t2= fuente2.render("Aciertos",True,(0,0,0),(255,255,255)) 
        ventana.blit(t2,(820,123)) 
        
        t3= fuente2.render("Ptos",True,(0,0,0),(255,255,255))  
        ventana.blit(t3,(836,205))
        
        #IMPRECION DE LOS ACIERTOS
        acierto = fuente2.render(str(aciertos)+"/10",True,(0,0,0),(255,255,255))
        ventana.blit(acierto,(835,150))     
        
        #FUENTE Y IMPRECION DEL PUNTAJE EN PANTALLA
        punt= fuente2.render(str(total),True,(0,0,0),(255,255,255))
        ventana.blit(punt,(850,230))#punatje en pantalla
        
        #CONTADOR
        
        conta1= str(cont/10)
        t4= fuente3.render(conta1,True,(0,0,0),(255,255,255))
        ventana.blit(t4,(847,55))
        if y >= 720:
            s2.play()
            y=0
            ordenpala+=1
            if str(y) in str(720):#se resta en el total negativo cuando BAJA LA PALABRA A 500!!!!!
                total-=10   
        
        
        #CONDICION SOBRE LA CONTINUIDAD DEL JUEGO!!!!!!!!!!!!!!!!!   
        if str(10) in str(ordenpala):
            #CONVIERTO LA Y EN 0 O NEUTRA, PARA QUE NO DEJE CAER MAS NADA Y ME TIRE UN ERROR
            #YA Q EN LOS EVENT SE SUMAN + 1 LA PALABRA Y DEMASSSS
            y =0
            if aciertos >= 10 and total2 == 0:
                conta = 0
                carita1()
                
                #BINARIO DEL PUNTAJE
                puntaje = fuente1.render(str(resul),True,(r,g,b),(0,200,0))
                ventana.blit(puntaje,(400,550))
                
                #CARTEL O LETReRO
                t1= "PUNTUACION PERFECTA"
                letrero = fuente.render(t1,True,(r,g,b),(0,200,0)) 
                ventana.blit(letrero,(160,480))#CARPEL DE PALABRA PUNTAJE
               
                #CARTEL DE GANASTE
                ganaste = fuente1.render("ERES EL/LA MEJOR",True,(r,g,b),(0,200,0))
                ventana.blit(ganaste,(200,360))#IMPRECION BINARIO DEL PUNTAJE
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            ventana.blit(limpiar,(0,0))
                            
                            principal()#vuelve al menu principal
               
            
            else:
                
                carita2()
                #NUMERO BINARIO DLE PUNTAJE
                puntaje = fuente.render(str(total),True,(0,0,0),(0,200,0))
                ventana.blit(puntaje,(410,550))
        
                #LETRO DE PERDEDOR
                t= "PERDISTE"
                letrero1= fuente1.render(t,True,(0,0,0),(0,200,0)) 
                ventana.blit(letrero1,(295,360))
                
                #LETRORO DE LA SIGLA PUNTUACION
                p = "PUNTUACION"
                letrero2= fuente.render(p,True,(0,0,0),(0,200,0)) 
                ventana.blit(letrero2,(270,460))
                
                #EVENTO DEL RETORNO AL MENUUU!!!!
                for event in pygame.event.get():
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            ventana.blit(limpiar,(0,0))
                            principal()#vuelve al menu principal
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                        
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                     
                    if cadena == animales[ordenpala]:
                        
                        s1.play()
                        ordenpala+=1#cambio del orden de la palabra
                        cadena= ""
                        total+=10#se suma puntaje al conteo positivo
                        y=0
                        x+=70
                        aciertos+= 1  
                        
                        
                    else:
                        
                        y=0
                        s2.play()
                        total-=10   
                        cadena = ""
                        ordenpala+=1
                         
                elif event.key == pygame.K_BACKSPACE:     
                    if len(cadena)>0:
                            cadena = cadena[0:len(cadena)-1]
                else:
                    cadena = cadena + event.unicode 
        reloj.tick(22) 
        pygame.display.update()
    pygame.quit()

def juego():
  
    #agrego un string vacio porq sino me da error,tema de la siguiente palabra
    animales = ["tucan","tigre","foca","elefante","leon","jirafa","yacare","ballena","avestruz","delfin",""]
    ganaste = fuente1.render("GANASTE",True,(255,0,0),(0,0,0))
    perdiste = fuente1.render("PERDISTE",True,(255,0,0),(0,0,0))
    ordenpala=0
    ani1 = fuente.render(animales[ordenpala],True,(0,0,0),(255,255,255))
    reloj = pygame.time.Clock()
    fondo = pygame.image.load("juego/selva final1.JPG")
    
    #musica
    juego= pygame.mixer.music.load("juego/hakuna.mid")
    
    #sonidos
    s1= pygame.mixer.Sound("juego/ding.wav")#acierto en palabras
    s2= pygame.mixer.Sound("juego/chord.wav")#mal tipeado en palabras
    
    limpiar = ventana.copy()
    aciertos= 0
    total = 0
    total2 = 0
    #resul = total - total2
    cadena = ""
    y,x = 0,30 
    cont=0
    
    pygame.mixer.music.play()
    
    
    def carita1():
        
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))
        #RECTANGULO FONDO VERDE
        pygame.draw.rect(ventana,(0,200,0),(30,30,840,662),0)
        
        #CARITA
        pygame.draw.circle(ventana,(250,250,20),(435,200),100,0)#cabeza
        pygame.draw.circle(ventana,(255,255,255),(395,170),20,0)#ojo izquierdo
        pygame.draw.circle(ventana,(255,255,255),(480,170),20,0)#ojo derecho
        pygame.draw.circle(ventana,(0,0,0),(395,175),7,0)#yema izquierda
        pygame.draw.circle(ventana,(0,0,0),(480,175),7,0)#yema derecha
        pygame.draw.line(ventana,(0,0,0),(380,230),(400,260),5)
        pygame.draw.line(ventana,(0,0,0),(400,260),(440,265),5)
        pygame.draw.line(ventana,(0,0,0),(440,265),(470,257),5)
        pygame.draw.line(ventana,(0,0,0),(470,257),(488,231),5)
        pygame.draw.circle(ventana,(250,0,0),(435,200),10,0)#NARIZ
        
        pygame.draw.rect(ventana,(r,g,b),(688,642,182,50),2)#recuadre del s.NIVEL
        pygame.draw.rect(ventana,(r,g,b),(29,642,150,50),2)#recuadre del MENU
        #OPCIONES DE JUGADA 
        retorno= fuente3.render(" (M)Menu",True,(255,0,0),(0,200,0))
        ventana.blit(retorno,(30,648))
        
        #OPCION DE SIGUIENTE NIVEL
        juego= fuente3.render(" (S)Sig.Nivel",True,(255,0,0),(0,200,0))
        ventana.blit(juego,(690,648)) 
        
        reloj.tick(10)
        pygame.display.update()
    
    def carita2():
        
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))
        #RECTANGULO FONDO
        pygame.draw.rect(ventana,(0,200,0),(30,30,840,662),0)
        
        #CARITA
        
        pygame.draw.circle(ventana,(250,250,20),(435,200),100,0)#cabeza
        pygame.draw.circle(ventana,(255,255,255),(395,170),20,0)#ojo izquierdo
        pygame.draw.circle(ventana,(255,255,255),(480,170),20,0)#ojo derecho
        pygame.draw.circle(ventana,(0,0,0),(395,175),7,0)#yema izquierda
        pygame.draw.circle(ventana,(0,0,0),(480,175),7,0)#yema derecha
        pygame.draw.line(ventana,(0,0,0),(390,260),(420,250),5)
        pygame.draw.line(ventana,(0,0,0),(420,250),(455,250),5)
        pygame.draw.line(ventana,(0,0,0),(455,250),(482,260),5)
        pygame.draw.circle(ventana,(250,0,0),(435,200),10,0)#NARIZ 
       
        #recuadre del MENU
        pygame.draw.rect(ventana,(0,0,0),(29,645,140,47),2)
        
        #OPCION DE RETORNAR A MENU  
        retorno= fuente3.render(" (M)Menu",True,(255,0,0),(0,200,0))
        ventana.blit(retorno,(30,648))  
        
        
        reloj.tick(5)
        pygame.display.update()          
   
      
    while True:
        y +=10
        cont+=1
        resul = total + total2
        r= random.randrange(0,255)
        g= random.randrange(0,255)
        b= random.randrange(0,255)
        
        ventana.blit(limpiar,(0,0))
        ventana.blit(fondo,(0,0))
        
        #CAIDA DE LAS PALABRAS DE ANIMALESSSS
        ani1 = fuente.render(animales[ordenpala],0,(0,255,0))
        ventana.blit(ani1,(x,y))    
        
        #FUENTES DE LAS LETRAS TIPEADAS EN PANTALLA
        letras = fuente4.render(cadena,0,(0,255,0))
        ventana.blit(letras,(10,650)) 
        
        #CUADRO DE PUNTAJES VIDAS ETC
        pygame.draw.rect(ventana,(255,255,255),(810,20,90,80),0)
        pygame.draw.rect(ventana,(255,255,255),(810,120,90,60),0)
        pygame.draw.rect(ventana,(255,255,255),(810,200,90,60),0)
                
        t1= fuente2.render("Tiempo",True,(0,0,0),(255,255,255))
        ventana.blit(t1,(820,23)) 
        
        t2= fuente2.render("Aciertos",True,(0,0,0),(255,255,255)) 
        ventana.blit(t2,(820,123)) 
        
        t3= fuente2.render("Ptos",True,(0,0,0),(255,255,255))  
        ventana.blit(t3,(836,205))
        
        #IMPRECION DE LOS ACIERTOS
        acierto = fuente2.render(str(aciertos)+"/10",True,(0,0,0),(255,255,255))
        ventana.blit(acierto,(835,150))     
        
        #FUENTE Y IMPRECION DEL PUNTAJE EN PANTALLA
        punt= fuente2.render(str(total),True,(0,0,0),(255,255,255))
        ventana.blit(punt,(850,230))#punatje en pantalla
        
        #CONTADOR DE TIEMPO EN EL JUEGO
        
        
        conta1= str(cont/10)
        t4= fuente3.render(conta1,True,(0,0,0),(255,255,255))
        ventana.blit(t4,(847,55))
        
        #CONDICION SOBRE EL CAMBIO DE PALABRA Y SU SONIDO CORRESPONDIENTE
        if y >= 720:
            s2.play()
            y=0
            ordenpala+=1
            if str(y) in str(720):#se resta en el total negativo cuando BAJA LA PALABRA A 720!!!!!
                total-=10   
        
        #CONDICION SOBRE LA CONTINUIDAD DEL JUEGO!!!!!!!!!!!!!!!!!   
        if str(10) in str(ordenpala):
            #CONVIERTO LA Y EN 0 O NEUTRA, PARA QUE NO DEJE CAER MAS NADA Y ME TIRE UN ERROR
            #YA Q EN LOS EVENT SE SUMAN + 1 LA PALABRA Y DEMASSSS
            y =0
            conta= 0
            conta-=conta
            if aciertos >= 10 and total == 100:
                
                carita1()
                
                #BINARIO DEL PUNTAJE
                puntaje = fuente1.render(str(resul),True,(r,g,b),(0,200,0))
                ventana.blit(puntaje,(400,550))
                
                #CARTEL O LETReRO
                t1= "PUNTUACION PERFECTA"
                letrero = fuente.render(t1,True,(r,g,b),(0,200,0)) 
                ventana.blit(letrero,(160,480))#CARPEL DE PALABRA PUNTAJE
               
                #CARTEL DE GANASTE
                ganaste = fuente1.render("GANASTE",True,(r,g,b),(0,200,0))
                ventana.blit(ganaste,(310,360))#IMPRECION BINARIO DEL PUNTAJE
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            ventana.blit(limpiar,(0,0))
                            
                            cont=0
                            juego2()
                        if event.key == pygame.K_m:
                            cont=0
                            principal()
            else:
                
                carita2()
                #NUMERO BINARIO DEL PUNTAJE
                puntaje = fuente.render(str(total),True,(0,0,0),(0,200,0))
                ventana.blit(puntaje,(395,550))
        
                #LETRERO DE PERDEDOR
                t= "PERDISTE"
                letrero1= fuente1.render(t,True,(0,0,0),(0,200,0)) 
                ventana.blit(letrero1,(295,360))
                
                #LETRERO DE LA SIGLA PUNTUACION
                p = "PUNTUACION"
                letrero2= fuente.render(p,True,(0,0,0),(0,200,0)) 
                ventana.blit(letrero2,(270,460))
                
                
                #EVENTO DEL RETORNO AL MENUUU!!!!
                for event in pygame.event.get():
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_m:
                            cont =0
                            principal()
                            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                        
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                     
                    if cadena == animales[ordenpala]:
                        
                        s1.play()
                        ordenpala+=1#cambio del orden de la palabra
                        cadena= ""
                        total+=10#se suma puntaje al conteo positivo
                        y=0
                        x+=70
                        aciertos+= 1  
                        
                        
                    else:
                        
                        y=0
                        s2.play()
                        total-=10   
                        cadena = ""
                        ordenpala+=1
                #SE BORRA EN LA CADENA         
                elif event.key == pygame.K_BACKSPACE:     
                    if len(cadena)>0:
                            cadena = cadena[0:len(cadena)-1]
                #SE ESCRIBE
                else:
                    cadena = cadena + event.unicode 
        print cont
        reloj.tick(15) 
        pygame.display.update()
    pygame.quit()
pygame.mixer.music.play(10)

def principal():
    while True:
        
        
        main()  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:#opcion sobre el comienzo del juego
                    
                    juego()
                    
                if event.key == pygame.K_F2:#opcion sobre la ayuda en el juego
                    ayuda()
                    
                    
                if event.key == pygame.K_F3:#opcion de salir del juego
                    exit()
        
        reloj.tick(5)
        pygame.display.update()
    pygame.quit() 
principal()   