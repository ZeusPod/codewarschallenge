""" Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types. """

import string

s = "bitcoin take over the world maybe who knows perhaps"

def find_short (s):
    l = []
    s = s.split()
    long = []
    for p in s:
        l.append(p)

    for p in l:
        long.append(len(p))

    long.sort()    
    return(long[0])
    
me_string = find_short(s)
print(me_string)
