""" 
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
 
"""
import string


text = "The sunset sets at twelve o' clock."


def alphabet_position(text):
        alphabeths = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}
        return " ".join(str(alphabeths.get(char)) for char in text.lower() if char in alphabeths.keys())

    
    
    







me_replacewap = alphabet_position(text)
print(me_replacewap)
