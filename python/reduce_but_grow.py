def grow(arr):
    a = 1
    for n in arr:
        a = n * a

    return a


print(grow([1,4,9]))
