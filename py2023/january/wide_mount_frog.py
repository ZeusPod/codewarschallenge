import doctest


def mount_size(animal):
    """
    fuction to determine size a frog, this method takes one argument animal which corresponds to 
    the animal encountered by the frog. If this one is an alligator (case-insensitive) 
    return small otherwise return wide
    
    >>> mount_size('toucan'):
    'wide'
    
    >>> mount_size('ant bear'):
    'wide'
    
    >>> mount_size('alligator'):
    'small'

    """


    return 'wide' if animal.lower() != 'alligator' else 'small'

