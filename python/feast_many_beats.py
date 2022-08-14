def feast(beast, dish):
    if dish.startswith(beast[0]) and dish.endswith(beast[-1]):
        return(True)
    else:
        return(False)


