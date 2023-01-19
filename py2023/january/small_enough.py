"""
Se le dará una matriz y un valor límite. Debe verificar que todos los valores en la matriz
estén por debajo o sean iguales al valor límite. Si lo son, devuelve verdadero. 
De lo contrario, devuelve falso.
"""
import doctest


def small_enough(array, limit):
    """ small_enough test

    >>> small_enough([66, 101] ,200)
    True
     
    >>> small_enough([78, 117, 110, 99, 104, 117, 107, 115] ,100)
    False

    >>> small_enough([1, 1, 1, 1, 1, 2] ,1)
    False
    """
    return True if max(array) <= limit else False




doctest.testmod()
