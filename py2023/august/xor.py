import doctest

def xor(a,b):
    """
    funcion que evalua dos condiciones devolviendo verdadero si una de ellas 
    es True y false en caso contrario

    >>> xor(True, False)
    True
    >>> xor(False, True)
    True
    >>> xor(False, False)
    False
    """
   
    return a != b
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()


