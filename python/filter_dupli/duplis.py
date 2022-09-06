import doctest


def remove_duplicates(arr)->list:
    """
    this fuction remove duplicates in array
    
    >>> remove_duplicates([1,1,2,2,3,3,4])
    [1, 2, 3, 4]
   
    >>> remove_duplicates([16,5,3,16,1,16])
    [16, 1, 3, 5]
    

    """
    return list(set(arr))



doctest.testmod()


