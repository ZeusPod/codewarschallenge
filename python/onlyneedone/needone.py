import doctest

def check(seq, elem):
    """"
     >>> check([9,3,4,5], 5)
     True
     >>> check(["a",9,5,3,1],6)
     False
     >>> check([8,1,8,4,2,3],3)
     True
    """

    if elem in seq:
       return True
    else:
        return False



doctest.testmod()
