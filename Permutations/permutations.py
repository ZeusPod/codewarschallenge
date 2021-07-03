
import itertools

def permutations(string):
    perms = [''.join(i) for i in itertools.permutations(string)]
    perms1 = set(perms)
    return list(perms1)
         
    

string = ("aabb")

mi_permuta = permutations(string)
print(mi_permuta)



