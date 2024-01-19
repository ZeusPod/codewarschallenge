import doctest

def remove_first_last(string:str)->str:
    """
        funcion para eliminar el primer y ultimo
        carcater de un string cualquiera 
        
        >>> remove_first_last('1,2,3')
        '2'
        >>> remove_first_last('1,2,3,4')
        '2 3'
        >>> remove_first_last('1,2,3,4,5,6,7,8')
        '2 3 4 5 6 7'

    """
    if len(string) >= 3:
        list_str = string.split(',')
        last = len(list_str) -1
        x = slice(1,last)
        result=  " ".join(list_str[x])
        return result if result.strip() else None

    return None



if __name__ == "__main__":
    doctest.testmod()
     



