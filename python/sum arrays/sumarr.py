import doctest

def sum_array(a):
    """
    >>> sum_array([0])
    0
    >>> sum_array([1,2,3])
    6
    >>> sum_array([1.2,2.2,3.3])
    6.6
    """
    
    total = 0 
    if len(a) == 0:
        return 0
    else: 
        for i in a:
            total = total + i
        return round(total,2)


doctest.testmod()
