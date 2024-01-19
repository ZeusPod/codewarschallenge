import doctest
import math

def duty_free(price:int, discount:int, holiday_cost:int):
    """
    funcion para calcular cuantas botellas de whiskey se deben 
    comprar para a patir del descuento cubrir el costo de las 
    vaciones

    >>> duty_free(12,50,1000)
    166
    """
    return math.floor(holiday_cost / (price * discount / 100))

if __name__ == "__main__":
    doctest.testmod()


