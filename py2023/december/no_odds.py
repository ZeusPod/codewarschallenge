import doctest

def no_odds(values):
    """
    funcion que retorna todos los valores pares de un array

    >>> no_odds([0,1,2,3,4])
    [0, 2, 4]
    """
    return [x for x in values if x % 2 == 0]


if __name__ == "__main__":
     doctest.testmod()





