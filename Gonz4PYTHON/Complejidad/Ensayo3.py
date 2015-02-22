
def intercalar_listas():
    p1=[1,2,3,4,5,6,7,8]
    p2=[]
    p3=[]
    ini= 1
    
    if(p1!= [] and ini==1):
        for x in range(0,len(p1)):
            p2.append(p1[0])
            del p1[0]
        ini+=1    
        print p1,p2,p3
    
    if(p2!=[] and ini==2):#corrobora que hay algo en la lista y habilita a su trabajo
        for x in range(0,len(p2)):
            p3.append(p2[0])
            del p2[0]    
        print p1,p2,p3
    
def hanoi_iterativo(): #falta en la construccion
    torre1=[1,2,3,4,5,6]
    torre2=[]
    torre3=[]
    cabeza=0
    
    for maloso in range(0,6):
        if(torre1 != [] and torre2 == []):
            print "if"
            torre2.append(torre1[cabeza])
            del torre1[cabeza]
        
            
        elif(torre1[cabeza]> torre2[cabeza]):
            print "elif"
            torre3.append(torre1[cabeza])
            del torre1[cabeza]
        
        elif(torre2[cabeza]< torre3[cabeza]):
            temp=torre3
            torre3[cabeza]= torre2
            torre3.append(temp[cabeza])
            del torre2[cabeza]
        
        elif():
            pass
            
        print torre1,torre2,torre3 
    
def hanoi_recursivo():
    print 5


    
    
    
    
        

