import doctest


def how_much_i_love(nb_petals):
    """
    fuction to get the last position of de petals in a passionately game
    

    >>> how_much_i_love(3)
    'a lot'

    >>> how_much_i_love(6)
    'not at all'


    """




    petals = ["I love you","a little","a lot","passionately","madly","not at all"]
    if nb_petals <= 6:
        return petals[nb_petals -1]
    else:
        p = nb_petals % 6
        return petals[p -1] 

        
if __name__ == "__main__":
    doctest.testmod()




