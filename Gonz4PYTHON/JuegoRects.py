import pygame
import random

pygame.init()

ventana = pygame.display.set_mode([500,600])
pygame.display.set_caption("Rects")
reloj = pygame.time.Clock()

fuente= pygame.font.SysFont("Arial",30)
fuente2= pygame.font.SysFont("Arial",20)
termino = False
cronoint=0

r1 = pygame.Rect(50,50,50,50)
r2=pygame.Rect(250,350,150,50)
posx= random.randrange(50,400)
posy=random.randrange(20,500)
listarect=[]
for x in range(0,20):
    w= random.randrange(10,500)
    h=random.randrange(10,500)
    w1=random.randrange(20,30)
    h2=random.randrange(20,30)
    listarect.append(pygame.Rect(w,h,w1,h2))
r2=pygame.Rect(50,50,30,30)
limpiar= ventana.copy()
puntaje=0
while True:
    ventana.blit(limpiar,(0,0))#limpiar la pantalla
    if cronoint >= 10:
        termino = True   
    if termino == False:    
        cronoint = pygame.time.get_ticks()/1000
        crono2= str(cronoint)
        imprecion = fuente.render(crono2,0,(10,52,255))
    else:
        imprecion = fuente.render(crono2,0,(10,52,255))
            
    ventana.blit(imprecion,(450,10))
    t1= fuente.render(str(puntaje),0,(10,52,255))
    ventana.blit(t1,(450,40))
    
    texto="Tenes 10segundos para romper los Rects"
    t1=fuente2.render(texto,0,(255,255,255))
    ventana.blit(t1,(0,5))
    for z in listarect:
        
        pygame.draw.rect(ventana,(0,200,0),z)
              
        
    (r2.left,r2.top)= pygame.mouse.get_pos() 
    r2.left-=r2.height/2
    r2.top-=r2.width/2 
    pygame.draw.rect(ventana,(200,0,0),r2) 
    
   
    print puntaje   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:#si se preciona un boton del mouse
            for rect in listarect:
                if termino == False:#no el tiempo no llega a los 10seg
                    if r2.colliderect(rect):
                        rect.height=0
                        rect.width=0
                        puntaje+=10
                    
                
    
    
    
                
    reloj.tick(20)            
    pygame.display.update()
pygame.quit()    
                              