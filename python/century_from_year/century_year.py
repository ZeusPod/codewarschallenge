#funcion para calcular el siglo de acuerdo al año

def century(year):
    if (year % 100) == 0:
        return (year) // 100
    else: 
        return (year) // 100 + 1 

print(century(1601))
