import doctest

def find_mult_numbers(integer:int, limit:int)->list:
    """
    function to get multiples for a initial number in range

    >>> find_mult_numbers(5,25)
    [5, 10, 15, 20, 25]
    
    >>> find_mult_numbers(2,8)
    [2, 4, 6, 8]

    """

    numbers=[]
    for x in range(integer, limit + 1):
        if x % integer == 0:
            numbers.append(x)

    return numbers



doctest.testmod()
