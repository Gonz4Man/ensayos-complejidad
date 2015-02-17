#1)
def par(l):
    
    for x in l:
        if (x%2 ==0):
            print "numero par:",x
        else:
            print "numero impar:",x
# par([2,4,6,7,8,9,0,12,12,23,7])

def max_min():
    l2=[0,500000]
    lista =[]
    maximo =0
    minimo =0
    
    entrada = input("Ingrese cant. digits a ingresar :")
    for x in range(entrada):
        entrada2= input("ingrese un digito: ")
        lista.append(entrada2)
   
    for x in lista:
        if (x>l2[0]):
            
            l2[0] =x
        if (x< l2[1]):
           
            l2[1] =x
    print "maximo:",l2[0]
    print "minimo:",l2[1]
   
#max_min()

#3)
def palabra(pal):
    
    cant=0
    for x in pal:
        if (x== "a" or x== "e" or x== "i" or x== "o" or x== "u"):
            cant+=1
    print "cantidad de vocales: ", cant
 
#palabra("gonzalo")

#4)escribit un modulo que lea del teclado una cadena de carcateres
#e imprima la misma en orden inverso
def inversion(c):
    
    p=[]
    for x in c:
        print x
        p += x.pop()
    print p
#inversion("hola")

#5)

def codigo(pal):
    return pal[3:-2]
#print codigo("26-35111516-5")

def numbers(n):
    
    resultado=0
    if(n==0):        
        print "fin"
        
    else:
        
        resultado=n * numbers(n-1)
   
    return resultado
 
    
#print numbers(7)

#ejercicio combinatorio

        
     
#8)


def main():
    import pygame
    
    pygame.init()
    
    ventana= pygame.display.set_mode([400,400])
    pygame.display.set_caption("Ventana")
    reloj1 = pygame.time.Clock()
    salir = False 
    
   
    
    def cuadrado(n):
        w=0
        h=0
        x,y=0,0
        
        for x in range(1,n+1):
            
            pygame.draw.rect(ventana,(255,34,34),(180-x,180-y,50+w,50+h),0)
            w+=30
            h+=30
            x+=50
            y+=10
            
        pygame.display.update()
            
    def circulo(n):
        
        tamanio=0
        x,y=0,0
        
        for x in range(1,n+1):
            
            pygame.draw.circle(ventana,(255,34,34),(180+x,180+y),50-tamanio,3)
            
            
            x+=5
            y+=5
            tamanio+=2
        pygame.display.update()
        
    def lineas(n):
        w=0
        h=0
        x,y=0,0
        
        for x in range(1,n+1):
            
            pygame.draw.line(ventana,(255,34,34),(120+x,180+y),(50-w,50-h),2)
            w+=1
            h+=1
            x+=50
            y+=10
            
        pygame.display.update()
        
    print "a)funcion_cuadrado"
    print "b)Funcion_Circulo"
    print "c)Funcion_linea"
   
    entrada = raw_input("Ingrese opcion: ")
    entrada2= input("Ingrese cantidad n de apariciones:")
         
    if(entrada== "a"):
        cuadrado(entrada2)  
    if (entrada == "b"):
        circulo(entrada2)
    if(entrada == "c"):
        lineas(entrada2)
         
    while salir != True: #loop principal de eventos de la pantalla
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

        
            
        reloj1.tick(15)
        pygame.display.update()
    pygame.quit()
    
#main()

#10
def main2():
    import pygame
    
    pygame.init()
    
    ventana= pygame.display.set_mode([200,200])
    pygame.display.set_caption("Ventana")
    reloj1 = pygame.time.Clock()
    salir = False 
    
    fuente = pygame.font.Font(None,48)
    fuente2 = pygame.font.Font(None,15)
    texto1= fuente.render("par",0,(200,25,26)) 
    texto2= fuente.render("Impar",0,(200,25,26)) 
    texto3= fuente2.render("Precione un boton",0,(0,255,0)) 
         
    while salir != True: #loop principal de eventos de la pantalla
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
                
        ventana.blit(texto3,(10,10))
        ventana.blit(texto1,(70,50))
        ventana.blit(texto2,(70,110))
        
            
        reloj1.tick(15)
        pygame.display.update()
    pygame.quit()
    
