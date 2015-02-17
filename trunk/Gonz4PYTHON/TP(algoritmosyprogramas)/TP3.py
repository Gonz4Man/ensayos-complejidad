
#1)


def push(pila, elemento):
    
    pila.append(elemento)
    return pila
def Pop(pila):
    return pila.pop()
    
def isEmpty(pila):
    if (len(pila)>= 1):
        print "La pila contiene", len(pila), "elementos"
    else:
        print "La pila esta vacia"
def top(pila):
    
    return pila[-1:]

def size(pila):
    return len(pila)

def rever(pila):
    
    lista=[]
    for x in range(1,len(pila)+1):
        lista.append(pila[-x])
    return lista

def pushall(pila1,pila2):
    pila1 = pila2
    return pila1

#print push([],[0,1,2,3,4])
#print isEmpty([5])
#print top([0,1,2,4,5,87])
#print size([0,1,2,3])
#print rever([1,0,3,4])
#print pushall([],["Gonza"])


#2)
def invercion(l):
    resultado=""
    for x in range(1,len(l)+1):
        #implementado mediante la pila s slacing dentro de la misma
        resultado+=top(l[-x])
       
    print resultado
#invercion("hola")

#3)---------Cola-----------
def new():
    return []

def push_cola(cola,elemento):
    cola.append(elemento)
    return cola
def pop_cola(cola):
    del cola[0]
    return cola
def  isEmpty_cola(cola):
    
    if(len(cola) >= 1):
        
        print "La cola Tiene", len(cola),"Elementos"
    else:
        
        print "La cola esta vacia"

def first(cola):
    return cola[0]

def size_cola(cola):
    return len(cola)

def reverse(cola):
    lista=[]
    for x in range(1,len(cola)+1):
        lista.append(cola[-x])
    return lista
def pushall_cola(cola1,cola2):
    cola1 = cola2
    return cola1
cola =["gonzalo",24,"joaquin",23,"estefania",22]   
#print pop_cola(cola)
#print isEmpty_cola(cola)
#print first(cola)
#print size_cola(cola)
#print reverse(cola)
#print pushall_cola(["fede"],cola)


#4)
def sumar_colas(c1,c2):
    c3=0
    for x in c1:
        c3+=x
    for j in c2:
        c3+=j
    return c3
#print sumar_colas([50,20,1],[30,50,1])

#5)
def sumar_colas2(c1,c2,n,m):
    
    resultado =0
    if(n== len(c1)-1 and m == len(c2)-1):

        return 0
    
    if (m== len(c2)):
        return 0
    else:
        
        #el unico problema que se solo suma cundo hay listas de mismo tamanio
        suma =  c1[n]+ c2[m]
      
        resultado= suma +sumar_colas2(c1,c2,n+1,m+1)
        
        
    
        return resultado
#print sumar_colas2([1,1,1,1],[1,1,1],0,0)

#6)
def cadena_balanceda(cad):
    
 
        
    if (cad.count("(")and cad.count(")") == 1 ):
        print "esta balanceada"
    
    elif(cad.count("[")and cad.count("]") == 1 ):
        print "Esta balanceada"
    
    elif(cad.count("{") and cad.count("}") == 1 ):
        print "esta balanceada"

    else:
        print "No esta  balanceada"

#x=raw_input("Ingrese su cadena: ")
#cadena_balanceda(x)


#7)
#dejado por falta de ejemplos en el comportmiento de la funcion



      