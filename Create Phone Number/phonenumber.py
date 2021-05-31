""" Escriba una función que acepte una matriz de 10 enteros (entre 0 y 9), que devuelva una cadena de esos números en forma de número de teléfono. """


def create_phone_number(n):
   
    long = len(n)
    if long > 10:
        return False
    elif long < 10:
        return False
    elif long == 10:
        n = "".join(map(str, n))
        return "(" + n[0:3] + ")" + " " + n[3:6] + "-" + n[6:]


n = [1,2,3,4,5,6,7,8,9,0,]
mi_phone = create_phone_number(n)
print(mi_phone)