""" Complete la función scramble (str1, str2) que devuelve verdadero si una parte de los caracteres str1 puede reorganizarse para que coincida con str2; de lo contrario, devuelve falso. """

def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
            


s1 = 'rkqodlw'
s2 = 'world'

me_scramble = scramble(s1,s2)
print(me_scramble)