


def palrec(data):

    if(data == ""):#STRING VACIO
        return data
    else:
        return  palrec(data[1:])+data[0] 
        
print palrec("fede")
