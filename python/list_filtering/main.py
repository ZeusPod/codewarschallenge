import doctest


def filter_list(l:list)->list:
    """
    function to filter only int values of list
    
    >>> filter_list([1, 2, 'a', 'b'])
    [1, 2]
    >>> filter_list([1,'a','b',0,15])
    [1, 0, 15]

    """
    return [x for x in l if isinstance(x, int)]



