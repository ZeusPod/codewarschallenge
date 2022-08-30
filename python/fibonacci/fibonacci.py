import doctest

def fib(n:int)->int:
    """
    Funcion que obtiene el resultado fibonacci de un numero determinado
    
    >>> fib(8)
    21
    
    >>> fib(4)
    3
    """

    

    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n -2)

doctest.testmod()
