def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif n >= 1:
        square = 2 ** n 
        if square % 2 == 0:
            return True
        else:
            return False


n = int(input("Por favor introduce tu numero: "))
micuadrado = is_square(n)
print (micuadrado)
