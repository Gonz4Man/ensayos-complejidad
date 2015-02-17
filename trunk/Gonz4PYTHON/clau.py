import pygame

import random
pygame.init()
ventana = pygame.display.set_mode([1000,900])
pygame.display.set_caption("Laurita XXX")
reloj = pygame.time.Clock()
fuente= pygame.font.SysFont("Harrington", 40)
texto = fuente.render("(X)EXIT",True,(200,0,0),(0,0,0))
clau2 = pygame.image.load("you/clau2.png")
clau3 =pygame.image.load("you/clau8.png")
clau4 = pygame.image.load("you/clau9.png")
clau5 = pygame.image.load("you/clau11.png")
clau6 = pygame.image.load("you/clau12.png")
limpia = ventana.copy()
sonido = pygame.mixer.music.load("sonido/oscurodiamante.mp3")
sonido1 = pygame.mixer.Sound("sonido/ding.wav")

def xxx():
    pygame.mixer.music.play()
    salir = False
    while salir != True:
       
                     
        x= random.randrange(0,1000)
        y= random.randrange(0,900)
        m= random.randrange(0,1000)
        d= random.randrange(0,900)
        a= random.randrange(0,1000)
        b= random.randrange(0,900)
        f= random.randrange(0,1000)
        g= random.randrange(0,900)
        h= random.randrange(0,1000)
        i= random.randrange(0,900)
        j= random.randrange(0,1000)
        k= random.randrange(0,900)
        o= random.randrange(0,800)
        p= random.randrange(0,800)
        
        for n in range(0,200,5):
            
            ventana.blit(clau2,(m,d))
            ventana.blit(clau3,(a,b))
            ventana.blit(clau4,(f,g))
            ventana.blit(clau5,(h,i))
            ventana.blit(clau6,(o,p))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sonido1.play()
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    sonido1.play()
                    salir = True   
        ventana.blit(texto,(10,5))
        reloj.tick(15)
        pygame.display.update()
    pygame.quit()  
xxx()
