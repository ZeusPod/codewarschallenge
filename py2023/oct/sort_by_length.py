import doctest

def sort_by_length(array:list)->list:
    """
        funcion que recibe un array y devuelve el array ordenado 
        por el length de cada uno de sus items


        >>> sort_by_length(['beg', 'i', 'life', 'to'])
        ['i', 'to', 'beg', 'life']

        >>> sort_by_length(["beg", "life", "i", "to"])
        ['i', 'to', 'beg', 'life']

        >>> sort_by_length(["longer", "longest", "short"])
        ['short', 'longer', 'longest']


    """
    return sorted(array, key=len)




if __name__ == "__main__":
    doctest.testmod()



