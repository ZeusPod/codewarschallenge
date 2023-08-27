def round_to_next5(n):
    """
    Funcion para redondear cualquier numero a su subsiguiente multiplo de 5

    >>>round_to_next5(0)
    0
    >>>round_to_next5(6)
    10
    >>>round_to_next5(26)
    30
    >>>round_to_next5(20)
    """
    

    if(n<0):
        return 0 
    elif(n<5):
        return 5
    else:
        rest = n % 5
        complete = 5 - rest
        return n + complete

if __name__ == "__name__":
    import doctest
    doctest.testmod()
