def count_sheep(n):
    sheeps = [str(x)+' sheep...'for x in range(1,n +1)]
    return "".join(sheeps)


print(count_sheep(1))


