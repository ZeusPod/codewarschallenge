def tower_builder(n_floors:int):
    for i in range(n_floors):
        print(" "*(n_floors-i-1)+"*" *(2 * i+1))



tower_builder(5)
