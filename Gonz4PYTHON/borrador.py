
import pygame

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen =pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/mapa1.png")
        self.rect= self.imagen.get_rect()
    def update(self,ventana,vx,vy):
        #se mueve el fondo
        self.rect.move_ip(-vx,-vy)
        
        ventana.blit(self.imagen,self.rect)    
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.de1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/de1.PNG").convert()
        self.de2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/de2.PNG").convert()
        self.iz1= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/iz1.PNG").convert()
        self.iz2= pygame.image.load("C:/Documents and Settings/Gonz4lo/Escritorio/RPG/BOY1/iz2.PNG").convert()
        self.imagenes=[[self.de1,self.de2],[self.iz1,self.iz2]]
        self.imagen_actual = 0
        self.imagen= self.imagenes[self.imagen_actual][0]#AGARRA LA PRIMERA IMAGEN DE LA LISTA
        self.rect = self.imagen.get_rect()#Y ALA PRIMERA IMAGEN OBTENIDA LE AniADE SU RECTANGULO
        self.rect.top,self.rect.left = (230,240)
        self.moviendose = False
        self.orientacion = 0
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    
    def update(self,superficie,vx,vy,t):
        if (vx,vy)== (0,0) : self.moviendose = False
        else: self.moviendose = True # SE CUMPLE EN EL MOMENTO AL TOCAR UNA TECLA DE CORRIDO
        
        
        if vx >0: self.orientacion=0
        elif vx<0:self.orientacion=1
        
        if t == 1 and self.moviendose:
            self.nextimagen()
        vx=0
        vy=0
        self.mover(vx, vy)
        self.imagen= self.imagenes[self.orientacion][self.imagen_actual]
        superficie.blit(self.imagen,self.rect)    
    
    #ACA YA CAMBIARIA LAS IMAGENES DENTRO DE LA LISTA      
    def nextimagen(self):
        #EN LA IMAGEN ACTUAL ESTABA EN 0 Y LUEGO PASA A 1 ASY SUCESIVAMENTE
        self.imagen_actual+=1#ACA PASARIA EN LA SIGUIENTE TUPLA EN LA QUE SE MOVIESE
        
        #Si se va de rango se resetea a 0
        if self.imagen_actual > (len(self.imagenes)-1):
            self.imagen_actual=0     



def main():
    pygame.init()
     
    ventana= pygame.display.set_mode([500,500])
    pygame.display.set_caption("Player")
    rightsigueapretada,leftsigueapretada,upsigueapretada,downsigueapretada= False,False,False,False
    reloj = pygame.time.Clock()
    vx,vy= 0,0
    velocidad = 10
    
    jugador = Player()
    fondo= Fondo()
    t=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    upsigueapretada = True
                    vy-=velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada=True
                    vy+= velocidad 
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada=True
                    vx+=velocidad
                if event.key == pygame.K_LEFT:
                    leftsigueapretada=True
                    vx-=velocidad 
            
            if event.type == pygame.KEYUP:
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
        
        fondo.update(ventana, vx, vy)
        jugador.update(ventana,vx,vy,t)
        
        t+=1
        if t>1:
            t=0
        
        
                   
                 
        reloj.tick(25)
        pygame.display.update()
    pygame.quit()  
                    
main()                    
                        
    
