#crear una funcion que permita enmascarar los datos cvv de una tarjeta de credito y solo imprime los ultimos 4 numeros de la misma

def maskcvv(cc):
    long = len(cc)-4
    return((long * '#') + cc[-4:])
    



cc = input("Please introduce CC number: ").strip()
mycard = maskcvv(cc) 
print = mycard

