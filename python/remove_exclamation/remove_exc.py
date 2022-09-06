import doctest


def remove_exclamation_marks(s):
    """
    fuction to remove exclamation simbol for any string
    >>> remove_exclamation_marks('Hello World!')
    'Hello World'
    >>> remove_exclamation_marks('Good morning!')
    'Good morning'
    """
    return s.replace("!","")



doctest.testmod()
