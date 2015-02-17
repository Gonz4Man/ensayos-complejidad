import pygame
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.de1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/de1.PNG").convert_alpha()
        self.de2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/de2.PNG").convert_alpha()
        self.iz1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/iz1.PNG").convert_alpha()
        self.iz2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/iz2.PNG").convert_alpha()
        self.up1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/up1.PNG").convert_alpha()
        self.up2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/up2.PNG").convert_alpha()
        self.down1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/down1.PNG").convert_alpha()
        self.down2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/down2.PNG").convert_alpha()
        
        self.imagenes= [[self.de1,self.de2],[self.iz1,self.iz2],[self.up1,self.up2],[self.down1,self.down2]]
        self.imagen_actual= 0
        self.imagen = self.imagenes[self.imagen_actual][0].convert_alpha()
        self.rect = self.imagen.get_rect()
        self.rect.left,self.rect.top=(350,350)
        
        self.orientacion = 0
        self.moviendose= False
        
    def mover(self,vx,vy):
        
        self.rect.move_ip(vx,vy)
        
    def update(self,superficie,vx,vy,t):
        if (vx,vy)== (0,0) : self.moviendose = False
        else: self.moviendose = True # SE CUMPLE EN EL MOMENTO AL TOCAR UNA TECLA DE CORRIDO
        
        #CAMBIO DE LA TUPLA DE ORIENTACION EN LA IMAGEN DEPENDE DE LA TECLA TIPEADA
        
        if vx >0: self.orientacion=0
        elif vx<0:self.orientacion=1
        if vy<0:self.orientacion=2 
        elif vy >0: self.orientacion=3
        
        if t == 1 and self.moviendose:
            self.nextimagen()
        #ESTAS VARIABLES SON LA INMOVILIDAD DEL JUGADOR EN PANTALLA
#         vx=0
#         vy=0
        
        self.mover(vx, vy)
        self.imagen= self.imagenes[self.orientacion][self.imagen_actual]
        superficie.blit(self.imagen,self.rect)
    
    #ACA YA CAMBIARIA LAS IMAGENES DENTRO DE LA LISTA
    def nextimagen(self):
        #EN LA IMAGEN ACTUAL ESTABA EN 0 Y LUEGO PASA A 1 ASY SUCESIVAMENTE
        self.imagen_actual+=1#ACA PASARIA EN LA SIGUIENTE TUPLA EN LA QUE SE MOVIESE
        
        #Si se va de rango se resetea a 0  / EL MENOS(-3) ES EL RANGO MAXIMO DE LISTAS 
        #DE ESTA MANERA HAY  MOVILIDAD Y RECONOCIMIENTOS MEDIANTE LAS DEMAS TUPLAS "IMAGENES" 
        if self.imagen_actual > (len(self.imagenes)-3):
            self.imagen_actual=0 


class NPC(pygame.sprite.Sprite):
    def __init__(self):
        self.de1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/right.PNG").convert_alpha()
        self.de2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/right1.PNG").convert_alpha()
        self.iz1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/left.PNG").convert_alpha()
        self.iz2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/left1.PNG").convert_alpha()
        self.up1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/up.PNG").convert_alpha()
        self.up2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/up1.PNG").convert_alpha()
        self.down1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/down.PNG").convert_alpha()
        self.down2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY2/down1.PNG").convert_alpha()
        
        self.imagenes= [[self.de1,self.de2],[self.iz1,self.iz2],[self.up1,self.up2],[self.down1,self.down2]]
        self.imagen_actual= 0
        self.imagen = self.imagenes[self.imagen_actual][0].convert_alpha()
        self.rect = self.imagen.get_rect()
        self.rect.left,self.rect.top=(550,350)
        
        self.orientacion = 0
        self.moviendose= False
    
    def mover(self,x,y):
        self.rect.move_ip(x,y)
        
    def update(self,superficie,x,y,t):
        
        if (x,y)== (0,0) : self.moviendose = False
        else: self.moviendose = True # SE CUMPLE EN EL MOMENTO AL TOCAR UNA TECLA DE CORRIDO
            
        #CAMBIO DE LA TUPLA DE ORIENTACION EN LA IMAGEN DEPENDE DE LA TECLA TIPEADA
            
        if x >0: self.orientacion=0
        elif x<0:self.orientacion=1
        if y<0:self.orientacion=2 
        elif y >0: self.orientacion=3
            
        if t == 1 and self.moviendose:
            self.nextimagen()
            #ESTAS VARIABLES SON LA INMOVILIDAD DEL JUGADOR EN PANTALLA
           
        self.mover(x, y)
        self.imagen= self.imagenes[self.orientacion][self.imagen_actual]
            
        superficie.blit(self.imagen,self.rect)
    
    #ACA YA CAMBIARIA LAS IMAGENES DENTRO DE LA LISTA
    def nextimagen(self):
        #EN LA IMAGEN ACTUAL ESTABA EN 0 Y LUEGO PASA A 1 ASY SUCESIVAMENTE
        self.imagen_actual+=1#ACA PASARIA EN LA SIGUIENTE TUPLA EN LA QUE SE MOVIESE
        
        #Si se va de rango se resetea a 0  / EL MENOS(-3) ES EL RANGO MAXIMO DE LISTAS 
        #DE ESTA MANERA HAY  MOVILIDAD Y RECONOCIMIENTOS MEDIANTE LAS DEMAS TUPLAS "IMAGENES" 
        if self.imagen_actual > (len(self.imagenes)-3):
            self.imagen_actual=0 
          
        
class Pj(object):
    def __init__(self):
        self.hp=100
        self.max= self.hp
    def atacar(self): 
        self.danio= 5
        return self.danio
        
class NPC_IA(object):
    def __init__(self):
        self.hp=100
        self.max= self.hp
    def atacar(self):    
        self.danio= 5  


class Bola_de_Cristal(pygame.sprite.Sprite):
    def __init__(self):
        self.bola= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/Poderes/blue sphere.png")
        self.rect= self.bola.get_rect()
        self.rect.left,self.rect.top=0,0
       
    def update(self,superficie):
        superficie.blit(self.bola,self.rect)   






def main():
    pygame.init()
    ancho = 800
    alto=600
    ventana = pygame.display.set_mode([ancho,alto])
    pygame.display.set_caption("RPG")
    reloj = pygame.time.Clock()
    limpiar = ventana.copy()
    fuente = pygame.font.SysFont("Arial",20)
    #VARIABLES VELOCIDAD YA CON LAS MISMAS SE PUEDEN BUSCAR A DIFERENTES OBJETOS DETERMIANDOS
    vx,vy=0,0
    x,y=0,0 
    velocidad = 10
    termino = False
    distancia = 160
    
    jugador = Player()
    npc = NPC()
    playerstat= Pj()
    npcstat= NPC_IA()
    
    poder= Bola_de_Cristal()
    
    t=0
    t1=0
    termino = False
    #grupo_npc = pygame.sprite.Group(npc)
    #grupo_Player=pygame.sprite.Group(jugador)
    while True:
         
        ventana.fill([255,255,255])
        t+=1
        if t > 1:
            t=0
            t1=0
         
        #TENER EN CUENTA DONDE ESTAN POCICIONADOS LAS VARIABLES DE X,Y DE LA COLICION 
        #YA QUE EN LA MISMA SURGE EFECTO XD
        xold=jugador.rect.left
        yold=jugador.rect.top
        
        #LAS VARIABLES X E Y DEL PODER SOLAMENTE AL LLAMO CUANDO TIRO EL PODER
        #Y SE POCICIONA DESDE EL PUNTO DEL JUGADOR PARA DESPUES TIRAR
        def poderes():
            poder.rect.top = jugador.rect.top
            poder.rect.left = jugador.rect.left
        
        
        xnpc= npc.rect.left
        ynpc= npc.rect.top
       
        #HP EN PANTALLA SOBRE E JUGADOR
        vidanpc= fuente.render(str(npcstat.hp)+"/"+str(npcstat.max),0,(0,190,0))
        vidapj=fuente.render(str(playerstat.hp)+"/"+str(playerstat.max),0,(0,190,0))
        ventana.blit(vidanpc,(npc.rect.left-15,npc.rect.top-20))
        ventana.blit(vidapj,(jugador.rect.left-15,jugador.rect.top-25))
       
        #CODIGO SOBRE LA PERSECUCION  UNA DETERMINADA DISTANCIA
        # muy importante simplemente el "AND NOT", sino fuese asy lo sigue despues del ejex y no queremos eso xd
        if xold >= npc.rect.left-distancia and not xold >= npc.rect.left+distancia:
            if yold >= npc.rect.top-distancia and not yold >= npc.rect.top+distancia:
                if npc.rect.left > xold:
                    x-= 2#velocidad en la persecion
                elif npc.rect.left < xold:
                    x+= 2
                if npc.rect.top > yold:
                    y-= 2
                elif npc.rect.top < yold:
                    y+= 2 
                 
        
        jugador.update(ventana,vx,vy,t)
        npc.update(ventana, x, y, t)   
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_UP:
                    vy -=velocidad
                if event.key ==pygame.K_DOWN:
                    vy+=velocidad
                if event.key == pygame.K_LEFT:
                    vx-=velocidad
                if event.key == pygame.K_RIGHT:
                    vx+=velocidad
                if event.key == pygame.K_s :
                    
                    if jugador.orientacion== 0:
                        #PODER
                        #DE ENTRADA ANTES DE LA CONDICION DISPARA HACIA LE LADO X POSITIVO
                        poderes()
                        poder.update(ventana)
                        for x in range(0,120,1):
                            poder.rect.move_ip(x,0) 
                        
                    elif jugador.orientacion==1:
                        poderes()
                        poder.update(ventana)
                        poder.rect.move_ip(-10,0)
                    if jugador.orientacion== 2:
                        poderes()
                        #PODER
                        #DE ENTRADA ANTES DE LA CONDICION DISPARA HACIA LE LADO X POSITIVO
                        poder.update(ventana)
                        poder.rect.move_ip(0,-10)  
                    elif jugador.orientacion==3:
                        poderes()
                        poder.update(ventana)
                        poder.rect.move_ip(0,10)  
                 
                
                if  event.key == pygame.K_s and poder.rect.colliderect(npc):
                    if termino == False:
                        npcstat.hp-= playerstat.atacar()
                    if npcstat.hp == 0:
                        
                        termino =True 
                if jugador.rect.colliderect(npc.rect)and event.key == pygame.K_d  :
                    if termino == False :
                        npcstat.hp-= playerstat.atacar()     
                    if npcstat.hp == 0:
                        
                        
                        termino =True
            if event.type == pygame.KEYUP:
                
                if event.key== pygame.K_UP:
                    vy =0
                    
                if event.key ==pygame.K_DOWN:
                    vy=0
                    
                if event.key == pygame.K_LEFT:
                    vx=0
                    
                if event.key == pygame.K_RIGHT:
                    vx=0
                    
                if event.key == pygame.K_s:
                    if jugador.orientacion == 0:
                        poderes()
                        poder.rect.move_ip(120,0)
                        poder.update(ventana)
                    elif jugador.orientacion==1:
                        poder.rect.left = jugador.rect.left
                        poder.rect.top = jugador.rect.top
                        poder.rect.move_ip(-120,0)
                        poder.update(ventana)
                    if jugador.orientacion==2:
                        poderes()
                        poder.rect.move_ip(0,-120)
                        poder.update(ventana)
                    elif jugador.orientacion==3:
                        poderes()
                        poder.rect.move_ip(0,120)
                        poder.update(ventana)
                    
                    if  event.key == pygame.K_s and poder.rect.colliderect(npc):
                            if termino == False:
                                npcstat.hp-= playerstat.atacar()
                            if  jugador.rect.colliderect(npc.rect)and event.key == pygame.K_d :
                                    npcstat.hp-=playerstat.atacar()
                            
                            if npcstat.hp == 0:
                                termino =True
                  
                    
        #IMPORTANTE ESTAS VARIABLES (X,Y)IGUALADAS A 0 ,ASY EL NPC NO SE DE RANGO DRATICAMENTE
        #YA QUE DESPUES QUE SE MUEVA EL NPC SE MUEVA DE A POQUITO Y LENTAMENTE,SI ES QUE LO SACO
        #EL NPC SE VA DE RANGO Y HACE CUALQUIERA,(INCLUYE PERSONAJE CON ORIENTACION)
        x,y=0,0
       
        
        #COLICION ENTRE JUGADORES Y NO TOCARSE
        if jugador.rect.colliderect(npc.rect):
            jugador.rect.left,jugador.rect.top=xold,yold
            if npc.rect.colliderect(jugador.rect):
                npc.rect.left,npc.rect.top= xnpc,ynpc
                t=10 #HACE QUE EL JUGADOR NO SIGA CAMINANDO CUANDO COCA CON EL ADVERSARIO
        
        #PARA QUE NO SALGA DEL RANGO DE LA PANTALLA EL (JUGADOR)
        if jugador.rect.left <=0:
            jugador.rect.left=0
        elif jugador.rect.right >= ancho:
            jugador.rect.right = ancho
        if jugador.rect.top > alto:
            jugador.rect.top = alto
        elif jugador.rect.top <=0:
            jugador.rect.top=0
        
        reloj.tick(25)            
        pygame.display.update()
    pygame.quit()
                    
main() 
                   