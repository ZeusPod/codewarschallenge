""" escribir uan funcion que cuente la cantidad de veces que aparece cada letra en una cadena de caracteres """

from typing import Text


def count_char(text):
    char_freq = {}
    text = text.replace(" ", '')
    for c in text:
        if c in char_freq:
            char_freq[c] +=1
        else:
            char_freq[c] = 1
    
    return char_freq



text = "Hi how are things? How are you? Are you a developer? I am also a developer"

mychar = count_char(text)
print(mychar)