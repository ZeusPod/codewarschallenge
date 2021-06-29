
bonus = 5000
price = 3

def beeramid(bonus, price):
    beers = (bonus/price)
    levels = 0 

    while((levels + 1) ** 2 <= beers):
        levels += 1 
        beers -= levels * levels

    return levels     



mi_piramid = beeramid(bonus, price)
print(mi_piramid)