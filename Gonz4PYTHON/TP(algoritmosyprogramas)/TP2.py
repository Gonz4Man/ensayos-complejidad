

#1)
def Factorial(n):
   
    if(n==0): 
        resultado=1 
    else:   
        resultado= Factorial(n-1)
    
    return resultado
#Factorial(5)

#2)
def pal(string,n):

    if (n >= len(string)+1):
        return ""
    else:
          
        resultado = string[len(string)-n] + pal(string,n+1)

        return resultado
print pal("recurcion",1)




#3)
def factorial(n):
    
    if(n==1 or n==2):
        return 1
    
    elif(n>2):
        print "n:", n
        return(factorial(n-1) + factorial(n-2))
   
    
#print factorial(10) 
#4)
def maximo(lista,n):
    
    if(len(lista)<= 1 ):

        return
        
    else:
        
        valor=lista[0]
        print "valor y lista ", valor ,lista
        
        #si el valor copiado es menor intercambian y borra el menor asy sucesivamente
        if (valor < lista[1]):
            valor= lista[1]
            del lista[0]
           
        else:
            valor = valor
            del lista[1]
        
        maximo(lista,n)
    return lista 
    
#print maximo([2,4,1,10,5,745,8,12,14,45,78,79],0)

#5)

# ve el problema de que carajo no me devuelve la lista con los elementos sumados
def enteros(a,b,n):
    resultado =0
    if(n ==len(a)):# si le resto a len me da los resultados depende de los valores q en la lista tome
        return 0
    else:
        #en este ejemplo sumo todo los valores n de la lista
        suma=a[n] + b[n]
        resultado=enteros(a,b,n+1)+ suma
        
        return resultado     
        
#print enteros([2,4,6],[2,4,6],0)


#6)
def divicion(a,b):
    if (b<=a):
        return
    else:
        pass
#8)
def sumar_digitos(num,n):
    
    #Siempre se debe retirnar algo en la condicion base y el el cuerpo del if
    resultado= 0
    if(n ==len(str(num))):
        return 0
    
    else:
        convert = str(num)
        
        digito= int(convert[n])
        resultado += sumar_digitos(num,n+1) + digito
  
        return resultado

#print sumar_digitos(12,0)

#8)
#A))------EJEMPLO EJERCICIO A ---------------
#este ejemplo tiende a una recurcion infinita

#SOLUCION= PARA QUE NO DE RECURCION INFINITA DARLE UN VALOR SUPERIOR L DEL CASO BASE ENTERO POSITIVO MAYOR Q 1
def factorial2(n):
    if (n==0 or n==1):
        return 1
    else:

        return n* factorial2(n-1)
#nuf = factorial2(5)        
#print nuf

#B))------EJEMPLO EJERCICIO B ---------------
# en esta funcion no hay reircion infinita
def letras(letra):
    if (letra == "z"):
        print "z"
    else:
        oletra = raw_input("Ingrese letra (dentro de la funcion): ")
        print letra
        letras(oletra)
#letra = raw_input("Ingrese una letra")
#letras(letra)

#C))------EJEMPLO EJERCICIO C ---------------
#no hay recurcion infinita ya que el modulo random.random usa valores  0.etc menores por defecto que (1)
import random
def  rec(n):
    if (n<2):
        return 1
    else:
   
        n= random.random()
        
        return n* rec(n)
#numf2= rec(5)
#print numf2


#D))------EJEMPLO EJERCICIO D ---------------
#ESTE EJEMPLO TAMPOCO NOS DA UN RECURCION INFINITA YA QUE EN SUS CALCULOS MATEMATICOS DA EXACTO EL CASO BASE
import math

def recsc(n):
    if (n==1.0):
        return 1.0
    else:
        n= math.sqrt(math.sin(n)**2+math.cos(n)**2)
        return n * recsc(n)
#numf3= recsc(0.5)
#print numf3

#9)
#EJEMPLO ITERATIVO DEL FACTORIAL

def iterativo(n):
    
    resultado=0
    j=1
    for x in range(1,n):

        resultado= j*(x+1)
        j= resultado
        
    print "resultado: ",resultado 
#iterativo(7)

#10)
def promedio(lista,suma_total,cantidad):
   
    if(len(lista) == 0):
        print "fin"

        return suma_total/cantidad,[]
  
    else:
        valor_actual= lista[0]
        del lista[0]
        suma_total+= valor_actual
        cantidad+=1
        #tener en cuenta que en resultado es solamente un entero
        resultado=promedio(lista,suma_total,cantidad)
        
        #en la condicion saber que le mete una lista
        if (resultado[0]< valor_actual ):
            resultado[1].append(valor_actual)
        
        #entonces tiene que devolver una variable con un entero y una lista osea 0,[]
        
        return resultado
    
#print promedio([1,2,3,4],0,0)
    