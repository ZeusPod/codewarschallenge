#crear una funcion que valide un ISBN 
def isbnValidator(isbn):
    contador = 0
    suma = 0
    factor = 1
    
    if len(isbn) != 10:
        return False
        
    elif len(isbn) == 10:
        if isbn[0:8].isdigit() and (isbn[9] == 'X' or isbn[9] == 'x'):
            while contador <= 9:
                        suma =  sum + int(isbn[contador]) * factor
                        factor += 1
                        contador += 1
            if suma % 11 == 0:
                return True
            else:
                return False

        else:
            return False        

    else:
        return False     



print(isbnValidator('1293000000'))

""" contador = 0
suma = 0
factor = 1
isbn =  '1293000000'



while contador <= 9:
                suma += int(isbn[contador]) * factor
                factor += 1
                contador += 1
                
if suma % 11 == 0:
    print("El ISBN es valido")
else:
    print("El ISBN no es valido") """


