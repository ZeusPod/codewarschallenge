medi = []
with open('medicamentos.txt', 'r', encoding='utf-8') as m:
    lineas = m.readlines()
    lineas = list(map(lambda l: l.strip('\n'), lineas))
    for l in lineas:
        print(l)