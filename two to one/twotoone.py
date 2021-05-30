""" Tome 2 cadenas s1 y s2 que incluyan solo letras de la a a la z. Devuelve una nueva cadena ordenada, la más larga posible, que contenga letras distintas, cada una tomada solo una vez, provenientes de s1 o s2. """




a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"
def longest(a1,a2):
    c = []
    for caracter in a1:
        if caracter not in c:
            c.append(caracter) 
    for letter in a2:
        if letter not in c:
            c.append(letter)
    
    
    d = "".join(map(str, c))
    d = "".join(sorted(d))
    return d


me_string = longest(a1,a2)
print(me_string)