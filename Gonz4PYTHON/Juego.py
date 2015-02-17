import pygame  
import random
import time
class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen
        self.rect= self.imagen.get_rect()
        self.rect.left,self.rect.top= (100,300)#pocicion x e y del sprite e imagen
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)#muevo el rectangulo de la imagen
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)    

      
class Pj(object):
    def __init__(self):
        self.hp=100
        self.max= self.hp
        self.danio= 5
class NPC(object):
    def __init__(self):
        self.hp=100
        self.max=self.hp    
        self.danio=1
class Bola_de_Fuego(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen= imagen
        self.rect= self.imagen.get_rect()
        self.rect.left,self.rect.top= 100,100
       
    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)    
        
        
def main(): 
    
    pygame.init()
    ventana = pygame.display.set_mode([800,600])
    reloj = pygame.time.Clock()
    #IMAGENES EN PANTALLA
    imagen= pygame.image.load("c:/ball.png")
    imagen1= pygame.image.load("c:/pelota.png")
    imagen2=pygame.image.load("c:/1.png").convert_alpha()
    
    limpiar= ventana.copy()
    rightsigueapretada,leftsigueapretada,upsigueapretada,downsigueapretada= False,False,False,False
      
    #GESTOR DE VOLOCIDAD
    vx,vy=0,0
    velocidad=10
    
    
    player1= Player(imagen)  
    playerpj = Pj()#CLASE VIDA DEL JUGADOR
    npcplayer= NPC()#CLASE DE LA VIDA DEL NPC/ENEMIGO
    boladefuego = Bola_de_Fuego(imagen2)
    
    fuente= pygame.font.SysFont("Arial",25) 
    
    sprite = pygame.sprite.Sprite()
    sprite.imagen= imagen1
    
    sprite.rect= imagen1.get_rect()
    sprite.rect.top=300#pos y en pantalla
    sprite.rect.left=400#pos x en pamtalla
    
    termino = False
    mov = True
    
    #VARIABLES SOBRE LA EVASION Y PERSECUCION
    predadorx = sprite.rect.left
    predadory= sprite.rect.top
    distancia= 180
    
    while True: 
        
                  
        texto= fuente.render(str(playerpj.hp)+"/"+str(playerpj.max),0,(0,90,0))
        texto1= fuente.render(str(npcplayer.hp)+"/"+str(npcplayer.max),0,(0,90,0))
        
        #VALORES DEL EJE (X,Y),VARIBLES QUE GUARDAN SU POCICION ANTERIOR 
        #PARA PODER USARLAS PARA SU COLICION
        oldx= player1.rect.left
        oldy=player1.rect.top    
         
        ventana.blit(limpiar,(0,0))
        ventana.fill((255,255,255))  
        
        ventana.blit(sprite.imagen,sprite.rect)
        
        player1.mover(vx, vy)
        player1.update(ventana)
        
        #CODIGO SOBRE EL MANEJO DE COLICIONES Y LA PERDIDA DE LA VIDA DEL JUGADOR SOBRE LE ENEMIGO
        if player1.rect.colliderect (sprite):
            player1.rect.left =oldx
            player1.rect.top = oldy
            if termino == False:#condiciones sobre la resta de la vida
                playerpj.hp-=  npcplayer.danio
            if playerpj.hp == 0 :# si la vida es igual a o deja de restarse y no dar valores negativos
                termino = True
                print "PERDITES"
        
        #ATAQUE MANO A MANO DEL JUGADOR + SU COLICION Y PRECIONANDO LA TECLA "D"
        if player1.rect.colliderect(sprite) and event.key == pygame.K_d:
            if termino == False:
                npcplayer.hp-= playerpj.danio
            if npcplayer.hp == 0:
                termino = True    

            
        #LETREROS SOBRE EL HP DEL PLAYER Y NPC    
        ventana.blit(texto1,(sprite.rect.left+25,sprite.rect.top-30))#texto en la pelota
        ventana.blit(texto,(player1.rect.left-10,player1.rect.top-26))#texto en la bola en  movimiento
        
        #VARIBLES QUE TOMAN LA POCICION ORIGINAL DEL JUGADOR SIN ALTERAR LA AUTENTICA
        xplayer= player1.rect.left
        yplayer= player1.rect.top
        
        
        #CODIGO SOBRE LA PERSECUCIONA  UNA DETERMINADA DISTANCIA
        # muy importante simplemente el "AND NOT", sino fuese asy lo sigue despues del ejex y no queremos eso xd
        if xplayer >= sprite.rect.left-distancia and not xplayer >= sprite.rect.left+distancia:
            if yplayer >= sprite.rect.top-distancia and not yplayer >= sprite.rect.top+distancia:
                if sprite.rect.left > xplayer:
                    sprite.rect.left -= 1
                elif sprite.rect.left < xplayer:
                    sprite.rect.left += 1
                    
                if sprite.rect.top > yplayer:
                    sprite.rect.top-= 1
                elif sprite.rect.top < yplayer:
                    sprite.rect.top += 1
            

    
        #SI EL DEPREDADOR/ENEMIGO ESTA IGUALADA EN LA MISMA COORDENADA DE MI PJ Y PARA QUE 
        #NO SE QUEDE PEGADO SE AUMENTA LA DISTANCIA ENTRE AMBOS PARA PODER DESPEGARSE U EVADIRSE
        if sprite.rect.left == xplayer or sprite.rect.top == yplayer: 
            sprite.rect.top+=6 
            sprite.rect.left+=6
   
      
        #GESTIONANDO EJES DE BOLa DE FUEGO == EN LAS COORDENADAS DEL JUGADOR
        boladefuego.rect.left = xplayer
        boladefuego.rect.top=yplayer
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   exit()  
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    upsigueapretada= True
                    vy-=velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada= True
                    vy+=velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada= True
                    vx+=velocidad
                    
                if event.key == pygame.K_LEFT:
                    leftsigueapretada= True
                    vx-=velocidad
                
                if event.key == pygame.K_s:
#                     if xplayer <= sprite.rect.left :
#                         #DE ENTRADA ANTES DE LA CONDICION DISPARA HACIA LE LADO X POSITIVO
#                         boladefuego.update(ventana)
#                         boladefuego.rect.move_ip(250,0)
#                         
#                     #ATAQUE CON LA BOLA DE FUEGO
#                         if boladefuego.rect.colliderect(sprite.rect) and boladefuego.rect>=sprite.rect.left:
#                             if termino == False:
#                                 npcplayer.hp-=10 #LE QUITA DE HP
#                             if npcplayer.hp == 0:
#                                 termino = True 
#                                 print "Ja lO mataste a ese pelotudo xd" 
#                     else:
#                         boladefuego.update(ventana)
#                         boladefuego.rect.move_ip(-250,0)#DISPARA HACIA X NEGATIVO   
#                         if boladefuego.rect.colliderect(sprite.rect) and boladefuego.rect>=sprite.rect.left:
#                             if termino == False:
#                                 npcplayer.hp-=10 #LE QUITA DE HP
#                             if npcplayer.hp == 0:
#                                 termino = True 
#                                 print "Ja lO mataste a ese pelotudo xd"    
                    if boladefuego.rect <=  sprite.rect.top and  boladefuego.rect >= sprite.rect.left-20 and not boladefuego.rect >= sprite.rect.left+25  :
                        boladefuego.update(ventana)
                        boladefuego.rect.move_ip(0,250)
                    if boladefuego.rect >= sprite.rect.top and  boladefuego.rect >= sprite.rect.left-20 and not boladefuego.rect >= sprite.rect.left+25 :
                
                        boladefuego.rect.move_ip(0,-250)
                        boladefuego.update(ventana)    
            if event.type== pygame.KEYUP:
                if event.key == pygame.K_UP:
                    upsigueapretada=False
                    if downsigueapretada:vx=velocidad
                    else:vy=0
                if event.key == pygame.K_DOWN:
                    downsigueapretada=False
                    if upsigueapretada:vx=-velocidad
                    else:vy=0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=False
                    if leftsigueapretada:vx=-velocidad
                    else:vx=0
                    
                if event.key == pygame.K_LEFT:
                    leftsigueapretada=False
                    if rightsigueapretada:vx=velocidad
                    else: vx=0 
          
                if event.key == pygame.K_s:
                    pass
#                     #SI LA POCICON X DEL JUGADOR STA ANTES Q EL ENEMIGO, DISPARA HACIA +X
#                     if xplayer <= sprite.rect.left:
#                         boladefuego.rect.move_ip(250,0)#DISPARA HACIA X POSITIVO
#                         boladefuego.update(ventana)  
#                     
#                     #SI LA POCICION X DEL JUGADOR STA SUPERIOR, CASO CONTRARIO MAYOR POCICION
#                     else:
#                         boladefuego.rect.move_ip(-250,0) #DISPARA HACIA X NEGATIVO
#                         boladefuego.update(ventana)
#       
#                     if yplayer <=  sprite.rect.top and not xplayer >= sprite.rect.left+35  :
#                         
#                         boladefuego.rect.move_ip(0,250)
#                         boladefuego.update(ventana)
#                     if yplayer >= sprite.rect.top and not xplayer <= sprite.rect.left-35 :
#                         
#                         boladefuego.rect.move_ip(0,-250)
#                         boladefuego.update(ventana)         
#         
        reloj.tick(20)
        pygame.display.update()
    pygame.quit()
main()   
    
    
    
               