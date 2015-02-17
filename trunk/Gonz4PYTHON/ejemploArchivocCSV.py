# 
# archivo = open("texto2.txt","a")
# 
# lista = ["que haces","que contas gon","che que te parece un faso"]
# num = [1,2,3,11,55,4,1]
# 
# for x in range(0,10):
#     
#     letras = raw_input("Ingrese las lineas:")
#     archivo.write(letras+"\n")
#     
# archivo.close()
import csv

def write():
    abriendo2= open("archivo2.csv","w")
    leyendo = csv.writer(abriendo2)
    for x in range(0,5):
        lineas =raw_input("Escriba :")
    
        leyendo.writerow([lineas])
    
    abriendo2.close()

write()    
    
    
    
           