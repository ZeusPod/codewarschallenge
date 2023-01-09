def gimmer(a:list):
    b = []
    for x in a:
        b.append(x)
    b.sort()
    return a.index(b[1])

print(gimmer([1,5,4]))